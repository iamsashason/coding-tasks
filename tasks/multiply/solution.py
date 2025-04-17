#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.
# For matrix multiplication, the number of columns in A must be equal to the number of rows in B
# The resulting matrix will have the same number of rows as A and the same number of columns as B

def multiply(matrix_a, matrix_b): # Function to multiply two matrix.

    if not matrix_a or not matrix_b or len(matrix_a[0]) != len(matrix_b): # Checks if the matrices are valid for multiplication.
        raise ValueError("Invalid matrices for multiplication") # Raises an error if the matrices are not valid for multiplication.
    
    rows_a = len(matrix_a) # Number of rows in matrix A
    cols_a = len(matrix_a[0]) # Number of columns in matrix A
    cols_b = len(matrix_b[0]) # Number of columns in matrix B

    result = [[0] * cols_b for _ in range(rows_a)] # Initializes the result matrix with zeros. The result matrix will have the same number of rows as A and the same number of columns as B.

    for i in range(rows_a): # Iterates through each row of matrix A.
        for j in range(cols_b): # Iterates through each column of matrix B.
            for k in range(cols_a): # Iterates through each column of matrix A (or row of matrix B). 
                result[i][j] += matrix_a[i][k] * matrix_b[k][j] # Calculates the dot product of the i-th row of A and the j-th column of B and stores it in the result matrix.

    return result # Returns the resulting matrix after multiplication.

def main(): # Main function to execute the program.
    matrix_a = [[1, 2, 3], [4, 5, 6]] # Example matrix A
    matrix_b = [[7, 8], [9, 10], [11, 12]] # Example matrix B
    print(multiply(matrix_a,matrix_b)) # Expected result [[58, 64], [139, 154]]

    matrix_a = [[1, 2, 2], [3, 1, 1]] # Another example matrix A
    matrix_b = [[4, 2], [3, 1], [1, 5]] # Another example matrix B
    print(multiply(matrix_a,matrix_b)) # Expected result [[12, 14], [16, 12]]

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.