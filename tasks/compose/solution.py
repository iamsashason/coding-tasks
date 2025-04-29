#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def compose(f, g): # Function to compose two functions f and g.
    return lambda x: f(g(x)) # Returns a lambda function that applies g to x and then applies f to the result.

def main(): # Main function to execute the program.
    def add5(x): # Function to add 5 to a number.
        return x + 5
    def mul3(x): # Function to multiply a number by 3.
        return x * 3
    print(compose(mul3, add5)(1)) # Expected result: 18 (1 + 5 = 6, 6 * 3 = 18)

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.