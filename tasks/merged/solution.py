#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def merged(*dicts): # Function to merge multiple dictionaries into a single dictionary with sets as values.
    result = {} # Initialize an empty dictionary to store the merged result.
    for d in dicts: # Iterate over each dictionary passed as an argument.
        for key, value in d.items(): # Iterate over each key-value pair in the current dictionary.
            if key not in result: # If the key is not already in the result dictionary, initialize it.
                result[key] = set() # Initialize the value as an empty set.
            result[key].add(value) # Add the value to the set corresponding to the key in the result dictionary.
    return result # Return the merged dictionary with sets as values.

def main(): # Main function to execute the program.
    print(merged({'a': 1, 'b': 2}, {'b': 10, 'c': 100})) # {'a': {1}, 'b': {2, 10}, 'c': {100}}
    print(merged()) # {}

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.