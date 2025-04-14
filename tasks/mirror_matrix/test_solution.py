import unittest # Import the unittest module
from solution import mirror_matrix # Import the function from solution.py

class TestMirrorMatrix(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_even_columns(self): # Test case for a matrix with two columns
        matrix = [
            [1, 2],
            [3, 4]
        ]
        result = mirror_matrix(matrix) # Call the function to test
        expected = [ # Expected result after mirroring
            [1, 1],
            [3, 3]
        ]
        self.assertEqual(result, expected) # Check if the result matches the expected output

    def test_even_columns(self): # Test case for a matrix with two raws
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        result = mirror_matrix(matrix) # Call the function to test
        expected = [
            [1, 2, 2, 1],
            [5, 6, 6, 5]
        ]
        self.assertEqual(result, expected) # Check if the result matches the expected output

    def test_odd_columns(self): # Test case for a matrix with three columns
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        result = mirror_matrix(matrix) # Call the function to test
        expected = [
            [1, 2, 1],
            [4, 5, 4],
            [7, 8, 7]
        ]
        self.assertEqual(result, expected) # Check if the result matches the expected output

    def test_single_row(self): # Test case for a matrix with a single row
        matrix = [[1, 2, 3, 4]] # Matrix with one row
        result = mirror_matrix(matrix) # Call the function to test
        expected = [[1, 2, 2, 1]] # Expected result after mirroring
        self.assertEqual(result, expected) # Check if the result matches the expected output

    def test_single_row(self): # Test case for a matrix with a single column
        matrix = [ # Matrix with one column
            [1],
            [2],
            [3]
        ]
        result = mirror_matrix(matrix) # Call the function to test
        expected = [
            [1], 
            [2], 
            [3]
        ]
        self.assertEqual(result, expected) # Check if the result matches the expected output

    def test_empty_matrix(self): # Test case for an empty matrix
        matrix = [] # Empty matrix
        result = mirror_matrix(matrix) # Call the function to test
        expected = [] # Expected result is also an empty matrix
        self.assertEqual(result, expected) # Check if the result matches the expected output

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
