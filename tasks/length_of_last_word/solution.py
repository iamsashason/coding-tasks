#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def length_of_last_word(str):

    words = str.strip().split() # Splits the input string into a list of words.
    if not words: # Checks if the list is empty.
        return 0 # Returns 0 if there are no words.
    return len(words[-1]) # Returns the length of the last word in the list. 

def main(): # Main function to execute the program.
    print(length_of_last_word('')) # 0
    print(length_of_last_word('man in Black')) # 5
    print(length_of_last_word('hello, world!')) # 6
    print(length_of_last_word('hello\t\nworld')) # 5 
    print(length_of_last_word("hello world")) # 5
    print(length_of_last_word("Python is awesome ")) # 7
    print(length_of_last_word("one\ttwo\nthree ")) # 5
    print(length_of_last_word("   ")) # 0
    print(length_of_last_word("")) # 0

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.