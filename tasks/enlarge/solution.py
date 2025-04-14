#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def enlarge(image): # Function to enlarge a given image represented as a list of strings.
    enlarged = [] # Initialize an empty list to store the enlarged image.
    for row in image: # Iterate through each row of the input image.
        doubled_row = ''.join([char * 2 for char in row]) # Double each character in the row.
        enlarged.append(doubled_row) # Append the doubled row to the enlarged list.
        enlarged.append(doubled_row) # Append the doubled row again to create the vertical enlargement.
    return enlarged # Return the enlarged image.

def main(): # Main function to execute the program.
    print(enlarge('___ ___')) # Expected result: ['____  ____', '____  ____', '____  ____', '____  ____']
    print(enlarge('*** ***'
    '** **'
    '*** ***'))
    # Expected result:
    # ['********  ********',
    #  '********  ********',
    #  '****  ****',
    #  '****  ****',
    #  '********  ********',
    #  '********  ********']
    
if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.