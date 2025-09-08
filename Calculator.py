class Calculator:
    @staticmethod
    def convert_to_float(arr: list) -> list | None:
        """
        This method converts every element in arr into float, if an element is unconvertable, return None
        else, return the converted list
        """
        converted_list = []
        for v in arr:
            try:
                converted_list.append(float(v))
            except Exception:
                return None # the element is unconvertable, return None
        return converted_list
    
    @staticmethod
    def operation_handler(params: list) -> tuple[float | None, int]:
        """
        parameters: params, a row extracted from CSV files, contains a series of number followed by a operation
        output: a tuple with 2 elements, which has the form: (result, error code)

        This method takes a row of data from a CSV file, treats the last element as the operator, 
        and calls the corresponding calculation method based on the operator. 
        If the format is invalid or the operator is unrecognized, return the appropriate error code.
        """

        # if number of parameters < 3, then return Error 2
        if len(params) < 3:
            return (None,2) # Bad Number of Params
        
        operation = params.pop() # extract the last element
        match operation:
            case "add":
                return Calculator.addition(params)
            case "subtract":
                return Calculator.subtraction(params)
            case "multiply":
                return Calculator.multiplication(params)
            case "divide":
                return Calculator.division(params)
            case "exponentiate":
                return Calculator.exponentiation(params)
            case _: # if nothing matches, return Unknown Operator (3)
                return (None, 3)
            
    @staticmethod
    def addition(arr: list) -> tuple[float | None, int]:
        operands = Calculator.convert_to_float(arr) # convert into floats
        if operands is None:
            return (None, 4) # at least one element cannot be converted to float, return Unknown Error
        result = sum(operands)
        return (result, 0)

    @staticmethod
    def subtraction(arr: list) -> tuple[float | None, int]:
        operands = Calculator.convert_to_float(arr) # convert into floats
        if operands is None:
            return (None, 4) # at least one element cannot be converted to float, return Unknown Error
        result = operands[0]
        for v in range(1,len(operands)):
            result -= operands[v]
        return (result, 0)
    
    @staticmethod
    def multiplication(arr: list) -> tuple[float | None, int]:
        operands = Calculator.convert_to_float(arr) # convert into floats
        if operands is None:
            return (None, 4) # at least one element cannot be converted to float, return Unknown Error
        result = operands[0]
        for v in range(1,len(operands)):
            result *= operands[v]
        return (result,0)
    
    @staticmethod
    def division(arr: list) -> tuple[float | None, int]:
        operands = Calculator.convert_to_float(arr) # convert into floats
        if operands is None:
            return (None, 4) # at least one element cannot be converted to float, return Unknown Error
        # check number of params
        if len(operands) != 2:
            return (None, 2)
        # check if divide by 0
        if operands[1] == 0:
            return (None, 1)
        result = operands[0]/operands[1]
        return (result, 0)
    
    @staticmethod
    def exponentiation(arr: list) -> tuple[float | None, int]:
        operands = Calculator.convert_to_float(arr) # convert into floats
        if operands is None:
            return (None, 4) # at least one element cannot be converted to float, return Unknown Error
        # check number of params
        if len(operands) != 2:
            return (None, 2)
        result = operands[0]**operands[1]
        return (result, 0)