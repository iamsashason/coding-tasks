#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

import itertools # Imports the itertools module for creating iterators for efficient looping.

def ichunks(chunk_size, iterable): # Function to yield chunks of a specified size from an iterable.
    it = iter(iterable) # Creates an iterator from the iterable.
    while True: # Infinite loop to continuously yield chunks.
        chunk = list(itertools.islice(it, chunk_size)) # Gets a slice of the iterator of the specified chunk size.
        if len(chunk) == chunk_size: # Checks if the length of the chunk is equal to the specified chunk size.
            yield chunk # Yields the chunk if it is of the correct size.
        else: # If the length of the chunk is not equal to the specified chunk size.
            break # Breaks the loop to stop yielding chunks.

def main(): # Main function to execute the program.
    print(list(ichunks(2, [1, 2, 3, 4, 5]))) # Expected result [[1, 2], [3, 4]]
    stream = ichunks(3, itertools.count()) # Creates an infinite iterator that yields chunks of size 3 from an infinite count iterator.
    print(list(itertools.islice(stream, 10000, 10002))) # Prints the 10000th and 10001st chunks from the infinite iterator. Expected [[30000, 30001, 30002], [30003, 30004, 30005]] 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.