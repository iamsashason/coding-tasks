Implement a function filter_anagrams that finds all anagram words. The function takes a source word and an iterable of words to check, and returns a sequence of anagrams.
Your function should be able to find anagrams of any sequences, including lists and tuples. The solution should be as general as possible.
Examples: 
list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) # ['aabb', 'bbaa']
list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) # [' carer', 'racer']
list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])) # []
list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]])) # [[2, 1], [1, 2]]