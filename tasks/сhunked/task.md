Implement the chunked function, which takes a number and a sequence as input. The number that specifies the size of the chunk. The function must return a list consisting of chunks of the specified size. The list must be divided into list chunks, a string into strings, and a tuple into tuples!

Examples: 
chunked(2, ['a','b','c','d']) # [['a','b'],['c','d']]
chunked(3, ['a','b','c','d']) # [['a','b','c'],['d']]
chunked(3,'foobar') # ['foo','bar']
hunked(10, (42,)) # [(42,)]