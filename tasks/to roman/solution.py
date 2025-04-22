#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def to_roman(number): # Function to convert an integer to a Roman numeral.
    if not 1 <= number <= 3000: # Check if the number is within the valid range (1 to 3000).
        raise ValueError("Number must be between 1 and 3000") # Raise an error if the number is not in the valid range.

    roman_dict = { # Dictionary mapping integers to their corresponding Roman numeral representations.
        1000: 'M',
        900:  'CM',
        500:  'D',
        400:  'CD',
        100:  'C',
        90:   'XC',
        50:   'L',
        40:   'XL',
        10:   'X',
        9:    'IX',
        5:    'V',
        4:    'IV',
        1:    'I'
    }

    result = [] # List to store the Roman numeral characters as they are generated.
    for value in sorted(roman_dict.keys(), reverse=True): # Iterate over the keys of the dictionary in descending order.
        while number >= value: # While the number is greater than or equal to the current value.
            result.append(roman_dict[value]) # Append the corresponding Roman numeral to the result list.
            number -= value # Subtract the value from the number.

    return ''.join(result) # Join the list of Roman numeral characters into a single string and return it.

def main(): # Main function to execute the program.
    print(to_roman(1987))  # MCMLXXXVII
    print(to_roman(2024))  # MMXXIV
    print(to_roman(44))    # XLIV 

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.