#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def filter_anagrams(reference, candidates): # Function to filter anagrams from a list of candidates based on a reference word.
    ref_sorted = sorted(reference) # Sort the reference word to create a standard form for comparison.
    return filter(lambda x: type(x) == type(reference) and sorted(x) == ref_sorted, candidates) # Use a lambda function to filter candidates that match the sorted reference word.

def main(): # Main function to execute the program.
    print(list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))) # ['aabb', 'bbaa']
    print(list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))) # ['carer', 'racer']
    print(list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer']))) # []
    print(list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))) # [[2, 1], [1, 2]]


if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.