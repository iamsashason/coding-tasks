#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def compare_version(version1, version2): # Function to compare two version strings.
    major1, minor1 = map(int, version1.split('.')) # Split the version strings by '.' and convert to integers.
    major2, minor2 = map(int, version2.split('.')) # Split the version strings by '.' and convert to integers.

    if major1 != major2: # Compare the major version numbers.
        return 1 if major1 > major2 else -1 # Return 1 if major1 is greater, -1 if major2 is greater.
    if minor1 != minor2: # Compare the minor version numbers.
        return 1 if minor1 > minor2 else -1 # Return 1 if minor1 is greater, -1 if minor2 is greater.
    return 0 # Return 0 if both major and minor version numbers are equal.

def main(): # Main function to execute the program.
    print(compare_version("0.1","0.2")) # -1
    print(compare_version("0.2","0.1")) # 1
    print(compare_version("0.1","0.1")) # 0
    print(compare_version("0.2","0.21")) # -1
    print(compare_version("0.21","0.2")) # 1
    print(compare_version("5.0","4.0")) # 1
    print(compare_version("4.0","5.0")) # -1
    print(compare_version("51.0","51.0")) # 0
    print(compare_version("51.0","40.0")) # 1
    print(compare_version("40.0","51.0")) # -1
    print(compare_version("1.12","2.21")) # -1
    print(compare_version("2.21","1.12")) # 1
    print(compare_version("1.12","1.12")) # 0

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.