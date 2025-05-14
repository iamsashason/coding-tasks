Implement a histo function that takes a list or tuple of numbers as input and returns a histogram as a string, with the histogram columns separated by \n characters. Each column displays the number of occurrences of a number in the list: graphically using the specified characters and as a numeric value, except when the count is zero.
Optional parameters:
min_value — defines the minimum value for which the histogram is drawn. Not set by default, meaning the top column in the histogram corresponds to the minimum of the passed numbers.
max_value — defines the maximum value for which the histogram is drawn. Not set by default, meaning the bottom column in the histogram corresponds to the maximum of the passed numbers.
bar_char — the character used to create columns in the histogram. By default, #.
Use the built-in tool — Counter to solve this.
Examples: 
print(histo([1, 1, 3, 4, 5]))                                                                                                                               
1|## 2
2|
3|# 1
4|# 1
5|# 1

print(histo([1, 1, 3, 4, 5], bar_char = '*'))                                                                                                               
1|** 2
2|
3|* 1
4|* 1
5|* 1

print(histo([1, 1, 3, 4, 5], min_value = 3, max_value = 4))                                                                                                 
3|# 1
4|# 1

print(histo([], min_value = 1, max_value = 5))                                                                                                              
1|
2|
3|
4|
5|