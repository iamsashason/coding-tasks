#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def summary_ranges(nums): # Function to summarize ranges in a list of integers.
    if len(nums) < 2: # Checks if the length of the list is less than 2.
        return [] # Returns an empty list if the condition is met.

    result = [] # Initializes an empty list to store the result.
    start = nums[0] # Sets the start of the range to the first element of the list.
    prev = nums[0] # Sets the previous element to the first element of the list.

    for i in range(1, len(nums)): # Iterates through the list starting from the second element.
        if nums[i] == prev + 1: # Checks if the current element is consecutive to the previous one.
            prev = nums[i] # Updates the previous element to the current one.
        else: # If the current element is not consecutive to the previous one:
            if start != prev: # Checks if the start and previous elements are different.
                result.append(f"{start}->{prev}") # Appends the range to the result list in the format "start->prev".
            start = nums[i] # Updates the start of the range to the current element.
            prev = nums[i] # Updates the previous element to the current one.

    if start != prev: # After the loop, checks if the start and previous elements are different. 
        result.append(f"{start}->{prev}") # Appends the last range to the result list in the format "start->prev".

    return result # Returns the result list containing the summarized ranges.

def main(): # Main function to execute the program.
    print(summary_ranges([1,2,3])) # ['1->3']
    print(summary_ranges([0,1,2,4,5,7])) # ['0->2','4->5']
    print(summary_ranges([110,111,112,111,-5,-4,-2,-3,-4,-5])) # ['110->112','-5->-4']



if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.