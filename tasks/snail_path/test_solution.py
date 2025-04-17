import unittest # Import the unittest module
from solution import snail_path # Import the function from solution.py

class TestSnailPath(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_3x3_matrix(self): # Define a test method for a 3x3 matrix
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [
            [1, 2, 3],
            [6, 9, 8],
            [7, 4, 5]
        ]
        self.assertEqual(snail_path(matrix), expected)

    def test_3x4_matrix(self): # Define a test method for a 3x4 matrix
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        expected = [
            [1, 2, 3, 4],
            [8, 12, 11, 10],
            [9, 5, 6, 7]
        ]
        self.assertEqual(snail_path(matrix), expected)

    def test_single_row(self): # Define a test method for a single row matrix
        matrix = [[1, 2, 3, 4]]
        expected = [[1, 2, 3, 4]]
        self.assertEqual(snail_path(matrix), expected)

    def test_single_column(self): # Define a test method for a single column matrix
        matrix = [
            [1],
            [2],
            [3],
            [4]
        ]
        expected = [
            [1],
            [2],
            [3],
            [4]
        ]
        self.assertEqual(snail_path(matrix), expected)

    def test_empty_matrix(self): # Define a test method for an empty matrix
        with self.assertRaises(ValueError):
            snail_path([])

    def test_irregular_matrix(self): # Define a test method for an irregular matrix
        matrix = [
            [1, 2, 3],
            [4, 5],
            [6, 7, 8]
        ]
        with self.assertRaises(ValueError):
            snail_path(matrix)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
