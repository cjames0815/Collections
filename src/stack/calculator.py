from stack.stack import *

class calculator:
    @staticmethod
    def evaluate(expression: str):
        """Evaluates a specifed mathematical expression

        Args:
            expression (str): specified matematical expression

        Returns:
            float: result of the mathmatical expression
        """  
        # create stack to store numbers 
        numbers = stack()

        #create stack to stroe operations
        operations = stack()

        # loo through mathmatical expression a character at a time 
        for s in expression:
            # if current character in a number
            if(s.isnumeric()):
                #push it onto numbers stack
                numbers.push(float(s))
            else:
                # if current character is an operator
                if (s == '+' or s == '-' or s == '*' or s =='/'):
                    #push it onto the operators stack
                    operations.push(s)
                elif(s == ')'):
                    # if current character is a right parenthesis,
                    #evaluate stacks
                    calculator.evaluateStackTops(numbers,operations)
                elif(s != '('):
                    # exit if the current character is invalid
                    exit("Illegal input expression!")

        # exit if the numbers tack doesn't have one number
        if(numbers.size() != 1):
            exit("Illegal input expression!")

        #return result of expression
        return numbers.pop()
    
    @staticmethod
    def evaluateStackTops(numbers,operations):   
        """Applies an operation taken from a specified operations stack to
        two number taken from the specified numbers stack

        Args:
            numbers (stack): specified numbers stack
            operation (stack): specified operation stack        
            
        """
        #exit if the numbers stack has less than two number or the operations 
        # stack has less than one operation 
        if ((numbers.size()< 2) or operations.isEmpty()):
            exit("Illegal input expression!")

        # assign the number at the top of the numbers stack to operand2
        operand2 = numbers.pop()

        #assign the number at the top of the numbers stack to operand1
        operand1 = numbers.pop()

        #assign the operations at the top of the operations stacks to operator
        operator = operations.pop()

        if(operator == '+'):
            #if the operator is +, add operand1 and operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 + operand2)

        elif(operator == '-'):
            #if the operator is -, subtract operand1 from operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 - operand2)

        elif(operator == '*'):
            #if the operator is *, multiply operand1 and operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 * operand2)   

        elif(operator == '/'):
            #if the operator is /, divide operand1 and operand2
            # and push the result onto the numbers stack
            numbers.push(operand1 / operand2)
        else:
            # exit if the operator isn't valid
            exit("Illegal input expression!")               
       
               