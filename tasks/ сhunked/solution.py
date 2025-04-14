#!/usr/bin/env python3 # Shebang line to specify the interpreter for execution.

def chunked(size, sequence): # Defines a function named chunked that takes a size and a sequence (list, string, etc.) as arguments.
    if size <= 0: # Checks if the size is less than or equal to 0.
        raise ValueError("Chunk size must be greater than 0") # Raises an error if the chunk size is less than or equal to 0.

    if isinstance(sequence, str): # Checks if the sequence is a string.
        return [sequence[i:i+size] for i in range(0, len(sequence), size)] # Returns a list of substrings of the specified size.
    elif isinstance(sequence, list): # Checks if the sequence is a list.
        return [sequence[i:i+size] for i in range(0, len(sequence), size)] # Returns a list of sublists of the specified size.
    elif isinstance(sequence, tuple): # Checks if the sequence is a tuple.
        return [tuple(sequence[i:i+size]) for i in range(0, len(sequence), size)] # Returns a list of subtuples of the specified size.
    else: # If the sequence is not a string, list, or tuple.
        raise TypeError("Unsupported sequence type") # Raises an error if the sequence is not a string, list, or tuple.

def main(): # Defines the main function, which is used to run the program.
    print(chunked(2, ['a','b','c','d'])) # Calls the chunked function with a size of 2 and a list of characters, printing the result. Expects [['a','b'],['c','d']]
    print(chunked(3, ['a','b','c','d'])) # Calls the chunked function with a size of 3 and a list of characters, printing the result. Expects [['a','b','c'],['d']]
    print(chunked(3,'foobar')) # Calls the chunked function with a size of 3 and a string 'foobar', printing the result. Expects ['foo','bar']
    print(chunked(10, (42,))) # Calls the hunked function with a size of 10 and a tuple containing the number 42, printing the result. Expects [(42,)]

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # Calls the main function to execute the tests.
