#!/usr/bin/env python3

def triangle(n): # Function to generate the nth row of Pascal's triangle.
    if n == 0: # Base case: if n is 0, return the first row of Pascal's triangle.
        return [1]

    row = [1] # Initialize the first row of Pascal's triangle.
    for i in range(1, n + 1): # Iterate from 1 to n to generate the nth row.
        new_row = [1] # Start each new row with 1.
        for j in range(1, len(row)): # Iterate through the previous row to calculate the new row.
            new_row.append(row[j - 1] + row[j]) # Calculate the new value as the sum of the two values above it in the triangle.
        new_row.append(1) # End each new row with 1.
        row = new_row # Update the row to the new row.

    return row 

def main(): # Main function to execute the program.
    print(triangle(1))  # Print the first row of Pascal's triangle.
    print(triangle(2))  # Print the second row of Pascal's triangle.
    print(triangle(3))  # Print the third row of Pascal's triangle.
    print(triangle(4))  # Print the fourth row of Pascal's triangle.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.