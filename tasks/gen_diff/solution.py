#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def gen_diff(dict1, dict2): # Function to generate a diff between two dictionaries.
    result = {} # Initialize an empty dictionary to store the result.
    all_keys = set(dict1.keys()) | set(dict2.keys())  # Get all unique keys from both dictionaries.

    for key in all_keys: # Iterate through all unique keys.
        if key not in dict1: # If the key is not in dict1, it means it was added in dict2.
            result[key] = 'added' # Mark it as 'added'.
        elif key not in dict2: # If the key is not in dict2, it means it was deleted from dict1.
            result[key] = 'deleted' # Mark it as 'deleted'.
        elif dict1[key] != dict2[key]: # If the key is in both dictionaries but the values are different.
            result[key] = 'changed' # Mark it as 'changed'.
        else: # If the key is in both dictionaries and the values are the same.
            result[key] = 'unchanged' # Mark it as 'unchanged'.
    
    return result # Return the result dictionary containing the diff.

def main(): # Main function to execute the program.
    dict1 = {"one": "eon", "two": "two", "four": True}
    dict2 = {"two": "own", "zero": 4, "four": True}
    print(gen_diff(dict1, dict2)) # {'one': 'deleted', 'two': 'changed', 'four': 'unchanged', 'zero': 'added'}

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.