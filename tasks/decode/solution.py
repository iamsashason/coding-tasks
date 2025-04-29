#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

from functools import reduce # Importing the reduce function from functools module to apply a rolling computation to sequential pairs of values in a list.

def decode(signal: str) -> str: # Function to decode a signal represented as a string of characters.
    def decoder(): # Inner function to create a decoder.
        state = [signal[0]] # Initialize state with the first character of the signal.

        return lambda acc, curr: ( # Lambda function to process each character in the signal.
            acc + ('0' if curr == state[0] else state.__setitem__(0, curr) or '1') # 
        )

    if not signal: # Check if the signal is empty.
        return '' # Return an empty string if the signal is empty.

    return reduce(decoder(), signal[1:], '0') # Use reduce to apply the decoder function to the signal, starting with '0' as the initial value.

def main(): # Main function to execute the program.
    print(decode('|¯|____|¯|__|¯¯¯')) # Expected result '0111000111101100'

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.