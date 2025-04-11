#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def sum_of_intervals(*intervals): # Function to calculate the sum of intervals. * args allows passing a variable number of arguments.
    intervals = sorted(intervals, key=lambda x: x[0]) # Sort intervals based on the start time. Key and lambda function are used to extract the first element of each interval for sorting.
    merged_intervals = [] # List to store merged intervals.
    for current in intervals: # Iterate through each interval in the sorted list.
        if not merged_intervals: # If merged_intervals is empty, append the current interval.
            merged_intervals.append(current) # If merged_intervals is empty, append the current interval.
        else: # If merged_intervals is not empty, check if the current interval overlaps with the last merged interval.
            last = merged_intervals[-1] # Get the last merged interval.
            if current[0] <= last[1]: # Check if the current interval overlaps with the last merged interval.
                merged_intervals[-1] = [last[0], max(last[1], current[1])] # If they overlap, merge them by updating the end time of the last merged interval to the maximum end time of both intervals.
            else: # If they do not overlap, append the current interval to merged_intervals.
                merged_intervals.append(current) # Append the current interval to merged_intervals.
    total_length = sum(interval[1] - interval[0] for interval in merged_intervals) # Calculate the total length of all merged intervals by summing the difference between the end and start times of each interval.
    return total_length

def main(): # Main function to execute the program.
    print(sum_of_intervals([1,1])) # 0  
    print(sum_of_intervals([1,2],[50,100],[60,70])) # 51 
    print(sum_of_intervals([1,2],[5,10])) # 6  
    print(sum_of_intervals([4,7],[5,10],[50,100],[40,110])) # 76


if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.