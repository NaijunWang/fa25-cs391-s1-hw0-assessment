import csv, sys
from Calculator import Calculator

class CSVCalculatorHandler:
    history_record = ["input_file,operation,result,error\n"] # a list that records every line of result 

    def __init__(self):
        pass

    def process_csvs(self, filenames, output_prefix="output"):
        # traverse each file, use enumerate to get both the index and the filename
        for index, file in enumerate(filenames): 
            # read file
            with open(file,"r",newline="") as rf:
                output_record = [["result","error"]] # output_record variable documents contents of the outputfile for each input file being read
                
                reader = csv.reader(rf)
                for row in reader:
                    # get the result tuple as the form (result, error code)
                    result, error_code = Calculator.operation_handler(row.copy())
                    # update output record
                    if result is None:
                        result = ""
                    output_record.append([str(result),str(error_code)])
                    # update history record
                    operation = ",".join(row) # convert each row of csvfile into a string
                    self.save_to_history(file, operation, result, error_code)

            # generate output csv file
            OutputFileName = f"{output_prefix}_{index}.csv"
            with open(OutputFileName,"w",newline="") as wf:
                writer = csv.writer(wf)
                writer.writerows(output_record)

    def save_to_history(self, filename, operation, result, error_code):
        # this method add element to the class variable history_record
        self.history_record.append(f'{filename},"{operation}",{result},{error_code}\n')

    def history_export(self, export_filename):
        # this method create a txt file from the class variable history_record
        with open(export_filename,"w",newline="") as tf:
            tf.writelines(self.history_record)


if __name__ == '__main__':
    files = sys.argv[1:]
    instance = CSVCalculatorHandler()
    instance.process_csvs(files)
    instance.history_export("history.txt")