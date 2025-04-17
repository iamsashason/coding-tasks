#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

from collections import Counter # Importing the Counter class from the collections module to count hashable objects.

def visualize(coins, bar_char='$'): # Function to visualize the distribution of coin denominations.
    if not coins: # Check if the coins list is empty.
        raise ValueError("The coins list cannot be empty.") # Raise a ValueError if the list is empty.

    counter = Counter(coins) # Count the occurrences of each denomination in the coins list.
    seen = [] # List to keep track of unique denominations in the order they appear.
    for coin in coins: # Iterate through the coins list.
        if coin not in seen: # Check if the coin is not already in the seen list.
            seen.append(coin) # Add the coin to the seen list.

    max_height = max(counter.values()) # Find the maximum count of any denomination.

    lines = [] # List to store the lines of the visualization.
    for level in range(max_height, 0, -1): # Iterate from max_height down to 1.
        line = [] # List to store the current line of the visualization.
        for coin in seen: # Iterate through the seen denominations.
            if counter[coin] >= level: # Check if the count of the coin is greater than or equal to the current level.
                line.append(bar_char) # Append the bar character to the line.
            else: # If the count of the coin is less than the current level.
                line.append(" ") # Append a space to the line.
        lines.append(" ".join(line).rstrip()) # Join the line with spaces and remove trailing spaces.

    label_line = " ".join(str(coin) for coin in seen) # Create a label line with the denominations.
    lines.append(label_line) # Append the label line to the lines list.

    return "\n".join(lines) # Join all lines with newline characters and return the final visualization.

def main(): # Main function to execute the program.
    print(visualize([1, 2, 1, 3, 3, 3, 3, 1, 2, 2, 5, 5, 10])) 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.