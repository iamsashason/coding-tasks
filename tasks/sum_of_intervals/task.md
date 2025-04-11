Implement a sum_of_intervals function that takes a list of intervals as input and returns the sum of all interval lengths. This task uses only integer intervals from 1 to ∞, which are represented as lists. The first value of an interval will always be less than the second value. For example, the length of the interval [1, 5] is 4, and the length of the interval [5, 5] is 0. Intersecting intervals should be counted only once.

Examples:

>>> from solution import sum_of_intervals
>>> sum_of_intervals([1,1]) >>> 1
>>> sum_of_intervals([1,2],[50,100],[60,70]) >>> 51
>>> sum_of_intervals([1,2],[5,10]) >>> 6
>>> sum_of_intervals([4,7],[5,10],[50,100],[40,110]) >>> 76