import unittest # Import the unittest module
from solution import decode # Import the function from solution.py

class TestDecode(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic_case(self): # Define a test method to test the basic case
        self.assertEqual(decode('|¯|____|¯|__|¯¯¯'), '0111000111101100')
        
    def test_empty_signal(self): # Define a test method to test the empty signal case
        self.assertEqual(decode(''), '')

    def test_single_character_signal(self): # Define a test method to test the single character signal case
        self.assertEqual(decode('|'), '0')
        self.assertEqual(decode('¯'), '0')

    def test_signal_with_no_changes(self): # Define a test method to test the signal with no changes
        self.assertEqual(decode('|||||'), '00000')
        self.assertEqual(decode('¯¯¯¯¯'), '00000')

    def test_signal_with_full_changes(self): # Define a test method to test the signal with full changes
        self.assertEqual(decode('|¯|¯|¯|'), '0111111')

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
