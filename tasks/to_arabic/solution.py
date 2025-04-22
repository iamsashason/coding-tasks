#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def to_arabic(roman): # Function to convert a Roman numeral to an integer.
    roman_to_value = { # Dictionary mapping Roman numeral characters to their corresponding integer values.
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    valid_pairs = { # Set of valid Roman numeral pairs that can be subtracted.
        'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
    }

    invalid_patterns = ['IIII', 'VV', 'XXXX', 'LL', 'CCCC', 'DD', 'MMMM'] # List of invalid patterns in Roman numerals.
    for pattern in invalid_patterns: # Loop through each invalid pattern.
        if pattern in roman: # Check if the pattern is present in the Roman numeral string.
            return False # If an invalid pattern is found, return False.

    total = 0 # Variable to store the total value of the Roman numeral.
    prev_value = 0 # Variable to store the previous value for comparison.
    i = 0 # Index to iterate through the Roman numeral string.

    while i < len(roman): # Loop through the Roman numeral string.
        if roman[i] not in roman_to_value: # Check if the current character is a valid Roman numeral.
            return False 

        if i + 1 < len(roman) and roman[i] + roman[i + 1] in valid_pairs: # Check if the current and next character form a valid pair.
            total += roman_to_value[roman[i + 1]] - roman_to_value[roman[i]] #  Add the value of the pair to the total.
            i += 2 # Move to the next character after the pair.
        else: # If the current character is not part of a valid pair.
            curr_value = roman_to_value[roman[i]] # Get the value of the current character.
            if prev_value and curr_value > prev_value: # Check if the current value is greater than the previous value.
                return False  
            total += curr_value # Add the current value to the total.
            prev_value = curr_value # Update the previous value to the current value.
            i += 1 # Move to the next character.

    return total # Return the total value of the Roman numeral.

def main(): # Main function to execute the program.
    print(to_arabic('X'))         # 10
    print(to_arabic('IX'))        # 9
    print(to_arabic('IIII'))      # False 
    print(to_arabic('MCMXC'))     # 1990
    print(to_arabic('XM'))        # False 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.