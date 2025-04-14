Implement a function summary_ranges that finds contiguous increasing sequences of numbers in a list and returns a list listing them.

Examples:

summary_ranges([]) # []
summary_ranges([1]) # []
summary_ranges([1,2,3]) # ['1->3']
summary_ranges([0,1,2,4,5,7]) # ['0->2','4->5']
summary_ranges([110,111,112,111,-5,-4,-2,-3,-4,-5]) # ['110->112','-5->-4']


