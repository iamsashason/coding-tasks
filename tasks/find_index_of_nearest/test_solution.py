import unittest # Import the unittest module
from solution import find_index_of_nearest # Import the function from solution.py

class TestFindIndexOfNearest(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_empty_list(self): # Test case for an empty list
        self.assertIsNone(find_index_of_nearest(5, [])) # Check if the function returns None for an empty list

    def test_exact_match(self): # Test case for an exact match
        self.assertEqual(find_index_of_nearest(-3, [-7, -5, 4, 3, -3, -2, -4]), 4) # Check if the function returns the correct index for an exact match

    def test_positive_numbers(self): # Test case for positive numbers
        self.assertEqual(find_index_of_nearest(0, [15, 10, 3, 4]), 2) # Check if the function returns the correct index for a positive number

    def test_descending_list(self): # Test case for a descending list
        self.assertEqual(find_index_of_nearest(4, [7, 5, 3, 2]), 1) # Check if the function returns the correct index for a descending list

    def test_multiple_matches(self): # Test case for multiple matches
        self.assertEqual(find_index_of_nearest(4, [7, 5, 4, 4, 3]), 2) # Check if the function returns the correct index for multiple matches

    def test_negative_target_and_numbers(self): # Test case for negative target and numbers
        self.assertEqual(find_index_of_nearest(-10, [-12, -8, -9, -11]), 2) # Check if the function returns the correct index for negative target and numbers

    def test_multiple_equidistant_negatives(self): # Test case for multiple equidistant negatives
        self.assertEqual(find_index_of_nearest(-3, [-2, -4]), 0) # Check if the function returns the correct index for multiple equidistant negatives

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
