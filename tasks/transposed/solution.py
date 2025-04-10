#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def transposed(matrix): # Function to transpose a matrix.
    return [list(row) for row in zip(*matrix)] # Transpose the matrix using the zip function and list comprehension.

def main(): # Main function to execute the program.
    print(transposed([[1]]))  # [[1]]
    print(transposed([[1, 2], [3, 4]]))  # [[1, 3], [2, 4]]
    print(transposed([[1, 2], [3, 4], [5, 6]]))  # [[1, 3, 5], [2, 4, 6]]
    print(transposed(transposed([[1, 2]])))  # [[1, 2]]

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.