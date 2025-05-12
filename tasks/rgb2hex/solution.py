#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.
def rgb2hex(r, g, b): # Function to convert RGB values to hexadecimal color code.

    return "#{:02X}{:02X}{:02X}".format(r, g, b) # Format the RGB values as a hexadecimal string.
    return f"#{r:02x}{g:02x}{b:02x}" # Alternative formatting using f-string.

def main(): # Main function to execute the program.
    print(rgb2hex(36, 171, 0))  # '#24ab00'
    print(rgb2hex(r=36, g=171, b=0))  # '#24ab00'

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.