import unittest # Import the unittest module
from solution import hamming_weight # Import the is_continuous_sequence function from solution.py

class TestHammingWeught(unittest.TestCase): # Create a test case class that inherits from unittest.TestCase

    def test_invalid_input(self): # Test the function with invalid inputs
        self.assertFalse(hamming_weight(-1)) # Test a negative number
        self.assertFalse(hamming_weight('a')) # Test a string
        self.assertFalse(hamming_weight(1.5)) # Test a float
        self.assertFalse(hamming_weight([1, 2, 3])) # Test a list
        self.assertFalse(hamming_weight(None)) # Test None
        self.assertFalse(hamming_weight({1: 'a'})) # Test a dictionary
        self.assertFalse(hamming_weight(True)) # Test a boolean value

    def test_hamming_weight(self): # Test the function with a valid continuous sequence
        self.assertEqual(hamming_weight(0), 0)
        self.assertEqual(hamming_weight(4), 1)
        self.assertEqual(hamming_weight(101), 4)

if __name__ == '__main__': # Checks if the script is being run directly (not imported as a module).
    unittest.main() # If the script is run directly (not imported as a module), calls the main function to execute the program.
