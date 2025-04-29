#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def same_parity_filter(lst): # Function to filter a list based on the parity of the first element.
    if not lst: # Check if the list is empty.
        return [] # Return an empty list if the input list is empty.
    first_parity = lst[0] % 2 # Calculate the parity of the first element (0 for even, 1 for odd).
    return list(filter(lambda x: x % 2 == first_parity, lst)) # Filter the list based on the parity of the first element.

def main(): # Main function to execute the program.
    print(same_parity_filter([2, 0, 1, -3, 10, -2])) # Expected result [2, 0, 10, -2]
    print(same_parity_filter([-1, 0, 1, -3, 10, -2])) # Expected result [-1, 1, -3]

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.