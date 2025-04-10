import unittest # Import the unittest module
from solution import transposed # Import the transposed function from solution.py

class TestTransposed(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_transposed_0(self): # Define a test method for n = [[1]]
        self.assertEqual(transposed([[1]]), [[1]])

    def test_transposed_1(self): # Define a test method for n = [[1, 2], [3, 4]]
        self.assertEqual(transposed([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_transposed_2(self): # Define a test method for n = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(transposed([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_double_transpose(self): # Test double transposition
        self.assertEqual(transposed(transposed([[1, 2]])), [[1, 2]])    

if __name__ == '__main__':
    unittest.main()
