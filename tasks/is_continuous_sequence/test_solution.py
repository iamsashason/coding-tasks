import unittest # Import the unittest module
from solution import is_continuous_sequence # Import the is_continuous_sequence function from solution.py

class TestIsContinuousSequence(unittest.TestCase): # Create a test case class that inherits from unittest.TestCase

    def test_valid_continuous_sequence(self): # Test the function with a valid continuous sequence
        self.assertTrue(is_continuous_sequence([4, 5, 6, 7])) # Test a valid continuous sequence

    def test_valid_continuous_sequence_with_negatives(self): # Test the function with a valid continuous sequence with negative numbers
        self.assertTrue(is_continuous_sequence([-3, -2, -1, 0])) # Test a valid continuous sequence with negative numbers

    def test_non_continuous_sequence(self): # Test the function with a non-continuous sequence
        self.assertFalse(is_continuous_sequence([1, 3])) # Test a non-continuous sequence

    def test_single_element_sequence(self): # Test the function with a single element sequence
        self.assertFalse(is_continuous_sequence([10])) # Test a single element sequence

    def test_empty_sequence(self): # Test the function with an empty sequence
        self.assertFalse(is_continuous_sequence([])) # Test an empty sequence

    def test_sequence_with_non_integer(self): # Test the function with a sequence containing non-integer values
        self.assertFalse(is_continuous_sequence([1, 2, '3'])) # Test a sequence with a string

    def test_sequence_with_mixed_types(self): # Test the function with a sequence containing mixed types
        self.assertFalse(is_continuous_sequence([1, 2, None])) # Test a sequence with None

    def test_sequence_with_floats(self): # Test the function with a sequence containing float values
        self.assertFalse(is_continuous_sequence([1.0, 2.0, 3.0])) # Test a sequence with float values

    def test_boolean_values(self): # Test the function with a sequence containing boolean values
        self.assertFalse(is_continuous_sequence([True, 2, 3])) # Test a sequence with boolean values
        self.assertFalse(is_continuous_sequence([False, 1, 2])) # Test a sequence with boolean values

if __name__ == '__main__': # Checks if the script is being run directly (not imported as a module).
    unittest.main() # If the script is run directly (not imported as a module), calls the main function to execute the program.
