import unittest # Import the unittest module
from solution import multiply # Import the function from solution.py

class TestMultiply(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    
    def test_2x2_matrices(self): # Test case for multiplying two 2x2 matrices
        a = [[1, 2], [3, 4]]
        b = [[2, 0], [1, 2]]
        expected = [[4, 4], [10, 8]]
        self.assertEqual(multiply(a, b), expected) # Check if the result of the multiplication is as expected

    def test_3x2_and_2x3(self): # Test case for multiplying a 3x2 matrix with a 2x3 matrix
        a = [[1, 4], [2, 5], [3, 6]]
        b = [[1, 2, 3], [4, 5, 6]]
        expected = [
            [17, 22, 27],
            [22, 29, 36],
            [27, 36, 45]
        ] 
        self.assertEqual(multiply(a, b), expected) # Check if the result of the multiplication is as expected

    def test_identity_matrix(self): # Test case for multiplying with an identity matrix
        a = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        self.assertEqual(multiply(a, identity), a) # Check if the result of the multiplication is the same as the original matrix

    def test_incompatible_matrices(self): # Test case for incompatible matrices
        a = [[1, 2, 3], [4, 5, 6]]
        b = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            multiply(a, b) # Check if a ValueError is raised when trying to multiply incompatible matrices

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
