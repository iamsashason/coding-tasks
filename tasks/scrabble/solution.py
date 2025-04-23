#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.
from collections import Counter # Importing Counter from collections module to count hashable objects.

def scrabble(letters, word): # Function to check if a word can be formed from given letters.
    letters_counter = Counter(letters.lower()) # Count occurrences of each letter in the letters string.
    word_counter = Counter(word.lower()) # Count occurrences of each letter in the word string.
    return all(letters_counter[char] >= count for char, count in word_counter.items())

def main(): # Main function to execute the program.
    print(scrabble('quijibo', 'jib'))       # True
    print(scrabble('quijibo', 'quiz'))      # False
    print(scrabble('ReaCtIon', 'Action'))   # True
    print(scrabble('abc', 'abcd'))          # False

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.