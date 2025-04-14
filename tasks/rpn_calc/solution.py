#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def rpn_calc(tokens): # Function to evaluate a Reverse Polish Notation (RPN) expression.
    stack = [] # Initialize an empty stack to hold operands.
    for token in tokens: # Iterate through each token in the input list.
        if isinstance(token, (int, float)): # Check if the token is a number (int or float).
            stack.append(token) # Push the number onto the stack.
        elif token in ('+', '-', '*', '/'): # Check if the token is an operator.
            b = stack.pop() # Pop the top two operands from the stack.
            a = stack.pop() # Pop the next operand from the stack.
            if token == '+': # Check if the operator is addition.
                stack.append(a + b) # Push the result of addition onto the stack.
            elif token == '-': # Check if the operator is subtraction.
                stack.append(a - b) # Push the result of subtraction onto the stack.
            elif token == '*': # Check if the operator is multiplication.
                stack.append(a * b) # Push the result of multiplication onto the stack.
            elif token == '/': # Check if the operator is division.
                if b == 0: # Check if the divisor is zero.
                    raise ZeroDivisionError("Division by zero") # Raise an error if division by zero is attempted.
                stack.append(a / b) # Push the result of division onto the stack.
        else: # If the token is neither a number nor a valid operator.
            raise ValueError(f"Invalied token: {token}") # Raise an error for invalid token.
    
    if len(stack) != 1: # Check if the stack has exactly one element after processing all tokens.
        raise ValueError("Invalid RPN expression") # Raise an error if the stack does not have exactly one element.
    return stack[0] # Return the final result from the stack.

def main(): # Main function to execute the program.
    print(rpn_calc([1,2,'+',4,'*',3,'+'])) # 15
    print(rpn_calc([7,2,3,'*','-'])) # 1

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.