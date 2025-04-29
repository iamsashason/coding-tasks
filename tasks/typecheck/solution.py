#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def typecheck(func): # Decorator function to check the types of function arguments.
    def wrapper(*args, **kwargs): # Wrapper function to check types.
        annotations = func.__annotations__ # Get the annotations (type hints) of the function.
        for arg, value in kwargs.items(): # Iterate over keyword arguments.
            expected_type = annotations.get(arg) # Get the expected type from annotations.
            if expected_type and not isinstance(value, expected_type): # Check if the value is of the expected type.
                raise TypeError(f"Argument '{arg}' should be of type {expected_type}, but got {type(value)}.") # Raise TypeError if the type does not match.
        return func(*args, **kwargs) # Call the original function with the arguments.
    return wrapper # Return the wrapper function.

def main(): # Main function to execute the program.
    @typecheck # Apply the typecheck decorator to the function.
    def greet(name: str, age: int): # Function to greet a person with their name and age.
        print(f"Hello, {name}. You are {age} years old.") # Print a greeting message.

    greet(name="Alice", age=30) # Correct usage: name is a string and age is an integer.  
    greet(name="Alice", age="30") # Incorrect usage: age is a string instead of an integer, which will raise a TypeError. 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.