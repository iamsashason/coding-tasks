#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.
def find_index_of_nearest(number, numbers): # Function to find the index of the nearest number in a list.
    if not numbers: # Check if the list is empty.
        return None # Return None if the list is empty.
    
    distances = [abs(num - number) for num in numbers] # Calculate the absolute differences between each number in the list and the target number.
    min_distance = min(distances) # Find the minimum distance.
    
    return distances.index(min_distance) # Return the index of the first occurrence of the minimum distance.

def main(): # Main function to execute the program.
    print(find_index_of_nearest(2, []))  # None
    print(find_index_of_nearest(0, [15, 10, 3, 4]))  # 2
    print(find_index_of_nearest(4, [7, 5, 3, 2]))  # 1
    print(find_index_of_nearest(4, [7, 5, 4, 4, 3]))  # 2
    print(find_index_of_nearest(-3, [-7, -5, -3, -2, -4]))  # 2
    print(find_index_of_nearest(-10, [-7, -5, -3, -2, -4]))  # 0

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.