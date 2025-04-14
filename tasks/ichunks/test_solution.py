import unittest # Import the unittest module
import itertools # Import the itertools module for creating iterators for efficient looping.
from solution import ichunks # Import the function from solution.py

class TestIchunks(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_basic(self): # Define a test method for basic functionality
        self.assertEqual(list(ichunks(2, [1, 2, 3, 4, 5])), [[1, 2], [3, 4]]) # Check if the output of ichunks(2, [1, 2, 3, 4, 5]) is equal to [[1, 2], [3, 4]]

    def test_not_enough_elements(self): # Define a test method for not enough elements
        self.assertEqual(list(ichunks(2, [1, 2, 3, 4])), [[1, 2], [3, 4]]) # Check if the output of ichunks(2, [1, 2, 3, 4]) is equal to [[1, 2], [3, 4]]

    def test_empty(self): # Define a test method for empty input
        self.assertEqual(list(ichunks(3, [])), []) # Check if the output of ichunks(3, []) is equal to []

    def test_single_chunk(self): # Define a test method for a single chunk
        self.assertEqual(list(ichunks(2, [1, 2])), [[1, 2]]) # Check if the output of ichunks(2, [1, 2]) is equal to [[1, 2]]

    def test_incomplete_last_chunk(self): # Define a test method for an incomplete last chunk
        self.assertEqual(list(ichunks(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Check if the output of ichunks(3, [1, 2, 3, 4, 5, 6, 7, 8, 9]) is equal to [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_stream(self): # Define a test method for streaming input
        stream = ichunks(3, itertools.count(1))  # Creates an infinite iterator that yields chunks of size 3 from an infinite count iterator starting at 1.
        self.assertEqual(list(itertools.islice(stream, 3)), [[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # Check if the first three chunks from the infinite iterator are equal to [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
