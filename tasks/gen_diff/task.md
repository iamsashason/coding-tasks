Implement a gen_diff function that compares two dictionaries and returns the result of the comparison as a dictionary.
The keys of the resulting dictionary will be all the keys from the two input ones, and the value will be a string describing the differences:
added, deleted, changed, or unchanged.
Possible values:
• added — the key was not in the first dictionary, but was added to the second
• deleted — the key was in the first dictionary, but is not in the second
• changed — the key was present in both the first and second dictionary, but the values ​​are different
• unchanged — the key was present in both the first and second dictionary with the same values
Example:
dict1 = {"one": "eon", "two": "two", "four": True}
dict2 = {"two": "own", "zero": 4, "four": True}
print(gen_diff(dict1, dict2)) # {'one': 'deleted', 'two': 'changed', 'four': 'unchanged', 'zero': 'added'}