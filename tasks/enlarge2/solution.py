#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

from functools import reduce # Importing the reduce function from functools module to apply a rolling computation to sequential pairs of values in a list.
from itertools import chain # Importing the chain function from itertools module to combine multiple iterables into a single iterable.

def curry(f):
    return lambda x: lambda y: f(x, y) # Currying function to transform a function that takes multiple arguments into a series of functions that each take a single argument.

def compose(f):
    return lambda g: lambda x: f(g(x)) # Function to compose two functions, where the output of the second function is passed as input to the first function.

dup = lambda x: x + x # Function to duplicate a character or string.

pair = lambda x: [x, x] # Function to create a list of two identical elements from the input.

concat = lambda x: list(chain.from_iterable(x)) # Function to flatten a list of lists into a single list.

def enlarge2(image):
    return compose(lambda lines: concat(list(map(pair, lines))))(
        lambda image: list(map(lambda line: ''.join(map(dup, line)), image))
    )(image) # Function to enlarge an image represented as a list of strings by duplicating each character and each line.

def display(image):
    for line in image:
        print(line) # Function to display the image by printing each line.

def main(): # Main function to demonstrate the functionality of the script.
    glider = [' * ', '  *', '***'] # Example image represented as a list of strings.
    print("Original image:")
    display(glider) # Display the original image.
    print("\nEnlarged image:")
    display(enlarge2(glider)) # Display the enlarged image.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.