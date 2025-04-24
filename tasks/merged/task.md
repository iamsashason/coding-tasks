Implement a function merged that merges multiple dictionaries into a single dictionary. The function takes any number of arguments and returns a dictionary in which each key contains a set of unique values.

Example:
print(merged({'a': 1, 'b': 2}, {'b': 10, 'c': 100}))
# {'a': {1}, 'b': {2, 10}, 'c': {100}}

print(merged())  
# {}