#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def build_query_string(params): # Function to build a query string from a dictionary of parameters.
    return '&'.join(f"{key}={params[key]}" for key in sorted(params)) # Joins the key-value pairs into a query string format.

def main(): # Main function to execute the program.
    dictionary = {
        'per': 10, 
        'page': 1
        } # Example dictionary to be converted into a query string.
    print(build_query_string(dictionary)) # Expected result 'page=1&per=10'

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.