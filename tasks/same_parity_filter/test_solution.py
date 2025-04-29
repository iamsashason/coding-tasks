import unittest # Import the unittest module
from solution import same_parity_filter # Import the function from solution.py

class TestSameParityFilter(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_even_parity(self): # Define a test method to test even parity filtering
        self.assertEqual(same_parity_filter([2, 0, 1, -3, 10, -2]), [2, 0, 10, -2])

    def test_odd_parity(self): # Define a test method to test odd parity filtering
        self.assertEqual(same_parity_filter([-1, 0, 1, -3, 10, -2]), [-1, 1, -3])

    def test_empty_list(self): # Define a test method to test the case of an empty list
        self.assertEqual(same_parity_filter([]), [])

    def test_single_element(self): # Define a test method to test the case of a single element
        self.assertEqual(same_parity_filter([4]), [4])
        self.assertEqual(same_parity_filter([7]), [7])

    def test_mixed_parity(self): # Define a test method to test a mixed list of even and odd numbers
        self.assertEqual(same_parity_filter([2, 4, 6, 1, 3, 5]), [2, 4, 6])
        self.assertEqual(same_parity_filter([1, 3, 5, 2, 4, 6]), [1, 3, 5])

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
