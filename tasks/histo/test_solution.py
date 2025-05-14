import unittest # Import the unittest module
from collections import Counter # Importing Counter from collections module to count hashable objects.
from solution import histo # Import the function from solution.py

class TestHisto(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic(self): # Test the basic functionality of the histo function
        data = [1, 1, 3, 4, 5]
        expected = "1|## 2\n2|\n3|# 1\n4|# 1\n5|# 1"
        self.assertEqual(histo(data), expected)

    def test_custom_bar_char(self): # Test the histo function with a custom bar character
        data = [1, 1, 3, 4, 5]
        expected = "1|** 2\n2|\n3|* 1\n4|* 1\n5|* 1"
        self.assertEqual(histo(data, bar_char='*'), expected)

    def test_with_min_and_max(self): # Test the histo function with specified min and max values
        data = [1, 1, 3, 4, 5]
        expected = "3|# 1\n4|# 1"
        self.assertEqual(histo(data, min_value=3, max_value=4), expected)

    def test_empty_with_range(self): # Test the histo function with an empty data list and specified min and max values
        expected = "1|\n2|\n3|\n4|\n5|"
        self.assertEqual(histo([], min_value=1, max_value=5), expected)

    def test_single_value(self): # Test the histo function with a single value in the data list
        self.assertEqual(histo([7]), "7|# 1")

    def test_all_zeros(self): # Test the histo function with all zeros in the data list
        data = [0, 0, 0]
        expected = "0|### 3"
        self.assertEqual(histo(data), expected)

    def test_only_min_value_set(self): # Test the histo function with only min_value set
        data = [3, 3]
        expected = "2|\n3|## 2"
        self.assertEqual(histo(data, min_value=2), expected)

    def test_only_max_value_set(self): # Test the histo function with only max_value set
        data = [4, 5, 5]
        expected = "4|# 1\n5|## 2\n6|"
        self.assertEqual(histo(data, max_value=6), expected)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
