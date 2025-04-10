#!/usr/bin/env python3 # This line indicates that the script should be run using Python 3.

def find_longest_length(s): # Defines a function to find the length of the longest substring without repeating characters.
    start = 0 # Initializes the starting index of the substring.
    max_len = 0 # Initializes the maximum length of the substring found so far.
    used_chars = {} # Dictionary to store the last index of each character encountered.

    for i, char in enumerate(s): # Iterates through the string, getting both the index and character.
        if char in used_chars and used_chars[char] >= start: # Checks if the character has been seen before and is within the current substring.
            start = used_chars[char] + 1 # Updates the starting index to the next character after the last occurrence of the current character.
        used_chars[char] = i # Updates the last index of the character in the dictionary.
        max_len = max(max_len, i - start + 1) # Calculates the length of the current substring and updates max_len if it's greater than the previous max_len.

    return max_len # Returns the maximum length of the substring found.

def main(): # Defines the main function, which is used to run the program.
    print(find_longest_length('abcdeef')) # Tests the function with a sample input, returns 5.    
    print(find_longest_length('jabjcdel')) # Tests the function with another sample input, returns 7.    
    print(find_longest_length('aaaa')) # Tests the function with a string of repeated characters, returns 1.
    print(find_longest_length('')) # Tests the function with an empty string, returns 0.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # Calls the main function to execute the tests.
