#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

from collections import OrderedDict # Import OrderedDict from collections module

asks_registry = {} # Initialize an empty dictionary to store registered asks.

def asks (argname, prompt): # Define a decorator function to register asks.
    def decorator(func): # Define a nested decorator function
        if func not in asks_registry: # Check if the function is not already registered
            asks_registry[func] = OrderedDict() # Initialize an OrderedDict for the function
        asks_registry[func][argname] = prompt # Register the argument name and prompt
        return func # Return the original function
    return decorator # Return the decorator function 

def interactive(title): # Define a decorator function to make a function interactive.

    def decorator(func): # Define a nested decorator function
        def wrapper(): # Define a wrapper function
            print(title) # Print the title
            prompts = asks_registry.get(func, {}) # Get the prompts for the function
            kwargs = {} # Initialize an empty dictionary for keyword arguments
            for arg, prompt in prompts.items(): # Iterate over the prompts
                kwargs[arg] = input(prompt) # Get user input for each prompt
            result = func(**kwargs) # Call the original function with the user input as keyword arguments
            print(result) # Print the result
        return wrapper # Return the wrapper function
    return decorator # Return the decorator function

@interactive('Calculator') # Decorate the calc function to make it interactive with a title 'Calculator'.
@asks('x', 'Enter first number: ') # Register the first argument 'x' with a prompt.
@asks('y', 'Enter second number: ') # Register the second argument 'y' with a prompt.

def calc(x, y): # Define the calc function to perform addition.
    return int(x) + int(y) # Return the sum of x and y as integers.

def main(): # Main function to execute the program.
    calc() # Call the calc function to start the interactive calculator. 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.5
