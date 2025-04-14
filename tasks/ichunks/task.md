Implement a function ichunks that must take as arguments the size of the chunk (a positive integer) and the data source (an iterator). The function must return an iterator of lists of a given length containing elements from the data source.
Attention, this time you will need to form pieces of a strictly specified length! If there are not enough elements for the last piece (if the stream ends at all), then the entire piece is discarded!
Examples:
list(ichunks(2,[1,2,3,4,5])) # [[1,2],[3,4]]
stream = ichunks(3,itertools.count()) 
list(itertools.islice(stream,10000,10002)) # [[30000,30001,30002],[30003,30004,30005]]