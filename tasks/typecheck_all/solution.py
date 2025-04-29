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

def typecheck_all(func): # Decorator function to check the types of all function arguments. 
    def wrapper(*args, **kwargs): # Wrapper function to check types.
        annotations = func.__annotations__ # Get the annotations (type hints) of the function.
        errors = [] # List to store error messages.
        for arg, value in kwargs.items(): # Iterate over keyword arguments.
            if arg in annotations: # Check if the argument is in annotations.
                expected_type = annotations[arg] # Get the expected type from annotations.
                def fake(**kwargs): return None # Fake function to use for type checking.
                fake.__annotations__ = {arg: expected_type} # Set the annotations for the fake function.
                try: # Try to typecheck the argument.
                    typecheck(fake)(**{arg: value}) # Call the typecheck function with the fake function and the argument.
                except TypeError as e: # Catch TypeError if the type does not match.
                    errors.append(str(e)) # Append the error message to the errors list.
        if errors: # If there are any errors in the errors list.
            raise TypeError("\n".join(errors)) # Raise TypeError with all error messages.
        return func(*args, **kwargs) # Call the original function with the arguments.
    return wrapper # Return the wrapper function.

def main(): # Main function to execute the program.
    @typecheck_all # Apply the typecheck_all decorator to the function.
    def greet_all(name: str, age: int, city: str): # Function to greet a person with their name, age, and city.
        print(f"Hello, {name}. You are {age} years old and live in {city}.") # Print a greeting message.

    greet_all(name="Alice", age="thirty", city="New York") # Incorrect usage
    greet_all(name="Alice", age=30, city="New York") # Correct usage

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.