import unittest # Import the unittest module
from solution import to_roman # Import the function from solution.py

class TestToRoman(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic_numbers(self): # Test basic Roman numeral conversions
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(4), 'IV')
        self.assertEqual(to_roman(9), 'IX')
        self.assertEqual(to_roman(40), 'XL')
        self.assertEqual(to_roman(90), 'XC')
        self.assertEqual(to_roman(400), 'CD')
        self.assertEqual(to_roman(900), 'CM')

    def test_round_numbers(self): # Test round numbers in Roman numerals
        self.assertEqual(to_roman(10), 'X')
        self.assertEqual(to_roman(50), 'L')
        self.assertEqual(to_roman(100), 'C')
        self.assertEqual(to_roman(500), 'D')
        self.assertEqual(to_roman(1000), 'M')

    def test_complex_number(self): # Test complex Roman numeral conversions
        self.assertEqual(to_roman(1987), 'MCMLXXXVII')
        self.assertEqual(to_roman(2999), 'MMCMXCIX')
        self.assertEqual(to_roman(2024), 'MMXXIV')

    def test_min_max_values(self): # Test the minimum and maximum values for Roman numeral conversion
        self.assertEqual(to_roman(1), 'I')
        self.assertEqual(to_roman(3000), 'MMM')

    def test_invalid_values(self): # Test invalid values for Roman numeral conversion
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(ValueError):
            to_roman(-5)
        with self.assertRaises(ValueError):
            to_roman(3001)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
