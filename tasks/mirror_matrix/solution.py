#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def mirror_matrix(matrix): # Function to mirror a matrix.
    if not matrix: # Checks if the matrix is empty.
        return [] # Returns an empty list if the matrix is empty.

    for row in matrix: # Iterates through each row of the matrix.
        width = len(row) # Gets the width of the current row.
        mid = width // 2 # Calculates the midpoint of the row.
        for i in range(mid): # Iterates from the start of the row to the midpoint.
            row[-(i + 1)] = row[i] # Mirrors the elements by swapping the current element with its corresponding element from the end.

    return matrix # Returns the modified matrix.

def main(): # Main function to execute the program.
    matrix1 = [ # Example matrix to demonstrate the function.
    [1, 2, 3],
    [4, 5, 6]
    ]
    print(mirror_matrix(matrix1)) # Expected result: [[1, 2, 1], [4, 5, 4]]
    matrix2 = [ # Another example matrix to demonstrate the function.
    [1, 2, 3, 4],
    [5, 6, 7, 8]
    ]
    print(mirror_matrix(matrix2)) # Expected result: [[1, 2, 2, 1], [5, 6, 6, 5]]
    matrix3 = [ # Yet another example matrix to demonstrate the function.
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
    ]
    print(mirror_matrix(matrix3)) # Expected result: [[1, 2, 3, 2, 1], [6, 7, 8, 7, 6]]
    matrix4 = [ # Another example matrix to demonstrate the function.
    [1, 2],
    [3, 4]
    ]
    print(mirror_matrix(matrix4)) # Expected result: [[1, 1], [3, 3]]

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.