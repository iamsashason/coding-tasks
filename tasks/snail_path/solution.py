#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def snail_path(matrix): # Function to return the snail path of a given matrix.
    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix): # Check if the matrix is empty or not rectangular.
        raise ValueError("Input must be a non-empty rectangular matrix.") # Raise an error if the input is not a non-empty rectangular matrix.

    rows, cols = len(matrix), len(matrix[0]) # Get the number of rows and columns in the matrix.
    result = [[None] * cols for _ in range(rows)] # Initialize a result matrix with the same dimensions as the input matrix, filled with None.

    values = [] # List to store the values in spiral order.
    left, right, top, bottom = 0, cols - 1, 0, rows - 1 # Initialize the boundaries for the spiral traversal.

    while left <= right and top <= bottom: # While there are still elements to traverse in the matrix.
        for j in range(left, right + 1): # Traverse from left to right along the top row.
            values.append(matrix[top][j]) # Append the values to the list.
        top += 1 # Move the top boundary down.

        for i in range(top, bottom + 1): # Traverse from top to bottom along the right column.
            values.append(matrix[i][right]) # Append the values to the list.
        right -= 1 # Move the right boundary left.

        if top <= bottom: # Check if there are still rows to traverse.
            for j in range(right, left - 1, -1): # Traverse from right to left along the bottom row.
                values.append(matrix[bottom][j]) # Append the values to the list.
            bottom -= 1 # Move the bottom boundary up.

        if left <= right: # Check if there are still columns to traverse.
            for i in range(bottom, top - 1, -1): # Traverse from bottom to top along the left column.
                values.append(matrix[i][left]) # Append the values to the list.
            left += 1 # Move the left boundary right.

    idx = 0 # Index to track the position in the values list.
    for i in range(rows): # Fill the result matrix with the values in spiral order.
        for j in range(cols): # Traverse each row.
            result[i][j] = values[idx] # Assign the value from the values list to the result matrix.
            idx += 1 # Increment the index to move to the next value.

    return result # Return the filled result matrix.

def main(): # Main function to execute the program.
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(snail_path(matrix)) # Expected result [1, 2, 3], [6, 9, 8], [7, 4, 5]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(snail_path(matrix)) # Expected result [1, 2, 3, 4], [8, 12, 11, 10], [9, 5, 6, 7]
if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.
