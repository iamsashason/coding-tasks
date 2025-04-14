#!/usr/bin/env python3 # Specifies that the script should be run using Python 3 interpreter.

def hamming_weight(n): # Defines the function hamming_weight, which calculates the Hamming weight of a number.
    if not isinstance(n, int) or isinstance(n, bool) or n < 0: # Checks if n is not an integer or if it is a boolean or if it is negative.
        return False
    if n == 0: # Checks if n is 0.
        return 0
    binary = '' # Initializes an empty string to store the binary representation of n.
    while n > 0: # While n is greater than 0, convert n to binary.
        binary = str(n % 2) + binary # 
        n = n // 2 # Divides n by 2 and stores the quotient back in n.
    count = 0 # Initializes a counter to count the number of 1's in the binary representation.
    for i in binary: # Iterates through each character in the binary string.
        if i == '1': # Checks if the character is '1'.
            count += 1 # Increments the counter by 1 if the character is '1'.
    return count # Returns the Hamming weight of the number.

def main(): # Defines the main function, which is used to run the program.
    print(hamming_weight(0)) # Checks the Hamming weight of 0 and prints the result, which should be 0.    
    print(hamming_weight(4)) # Checks the Hamming weight of 4 and prints the result, which should be 1.    
    print(hamming_weight(101)) # Checks the Hamming weight of 101 and prints the result, which should be 4.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.