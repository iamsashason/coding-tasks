#!/usr/bin/env python3 # Specifies that the script should be run using Python 3 interpreter.

def is_continuous_sequence(seq): # Defines the function is_continuous_sequence, which checks if a sequence is continuous.
    if ( # Checks if the sequence is not a list, has a length less than 2, or contains non-integer values.
        not isinstance(seq, list) # Checks if seq is a list.
        or len(seq) < 2 # Checks if seq is a list and has a length less than 2.
        or not all(isinstance(x, int) and not isinstance(x, bool) for x in seq) # Checks if all elements in seq are integers and not booleans.
    ):
        return False # Checks if seq is a list, has a length greater than 1, and contains only integers (not booleans).

    sorted_seq = sorted(seq) # Sorts the sequence in ascending order.
    for i in range(1, len(sorted_seq)): # Iterates over the elements of the sorted sequence, starting from index 1.
        if sorted_seq[i] - sorted_seq[i - 1] != 1: # Checks if the difference between the current element and the previous one is not equal to 1.
            return False # If the difference between the current element and the previous one is not 1, the sequence is not continuous.
    return True # If all elements of the sequence have been checked and there are no gaps, returns True.

def main(): # Defines the main function, which is used to run the program.
    print(is_continuous_sequence([4, 5, 6, 7]))     # Checks if the sequence [4, 5, 6, 7] is continuous and prints the result True.
    print(is_continuous_sequence([1, 2, 4]))        # Checks if the sequence [1, 2, 4] is continuous and prints the result False.
    print(is_continuous_sequence(["a", "b", "c"]))  # Checks if the sequence ["a", "b", "c"] is continuous and prints the result False, as the sequence consists of non-numeric values.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.
