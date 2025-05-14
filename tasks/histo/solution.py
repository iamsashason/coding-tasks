#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

from collections import Counter # Importing Counter from collections module to count hashable objects.

def histo(data, min_value=None, max_value=None, bar_char='#'): # Function to create a histogram from the given data.
    counts = Counter(data) # Counting the occurrences of each value in the data.
    
    if data: # Check if data is not empty
        if min_value is None: # If min_value is not provided, set it to the minimum value in data
            min_value = min(data) 
        if max_value is None: # If max_value is not provided, set it to the maximum value in data
            max_value = max(data)
    else: # If data is empty, set min_value and max_value to 0
        if min_value is None:
            min_value = 0
        if max_value is None:
            max_value = 0

    lines = [] # List to store the lines of the histogram.
    for i in range(min_value, max_value + 1): # Loop through the range from min_value to max_value (inclusive).
        count = counts.get(i, 0) # Get the count of the current value, defaulting to 0 if not found.
        bar = bar_char * count # Create a bar of the specified character repeated 'count' times.
        if count > 0: # If the count is greater than 0, create a line with the value and its corresponding bar.
            lines.append(f"{i}|{bar} {count}") # Format the line with value, bar, and count.
        else: # If the count is 0, create a line with just the value and a bar of spaces.
            lines.append(f"{i}|") # Format the line with value and an empty bar.
    
    return '\n'.join(lines) # Join all lines with newline characters to create the final histogram string.

def main(): # Main function to execute the program.
    print(histo([1, 1, 3, 4, 5]))
    # 1|## 2
    # 2|
    # 3|# 1
    # 4|# 1
    # 5|# 1
    print('\n')
    print(histo([1, 1, 3, 4, 5], bar_char='*'))
    # 1|** 2
    # 2|
    # 3|* 1
    # 4|* 1
    # 5|* 1
    print('\n')
    print(histo([1, 1, 3, 4, 5], min_value=3, max_value=4))
    # 3|# 1
    # 4|# 1
    print('\n')
    print(histo([], min_value=1, max_value=5))
    # 1|
    # 2|
    # 3|
    # 4|
    # 5|

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.