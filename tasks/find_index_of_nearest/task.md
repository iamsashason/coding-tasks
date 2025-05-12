Implement the find_index_of_nearest function that takes a list of numbers and the desired number as input. The function's task is to find the closest number to the desired number in the list and return its index.
If the list contains several numbers that are simultaneously closest to the desired number, then the smallest of the closest number indices is returned.
Examples:
find_index_of_nearest(2, []) # None
find_index_of_nearest(0, [15, 10, 3, 4]) # 2
find_index_of_nearest(4, [7, 5, 3, 2]) # 1
find_index_of_nearest(4, [7, 5, 4, 4, 3]) # 2