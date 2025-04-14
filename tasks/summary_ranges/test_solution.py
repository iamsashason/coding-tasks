import unittest # Import the unittest module
from solution import summary_ranges # Import the function from solution.py

class TestSummaryRanges(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_empty_list(self): # Test case for an empty list
        self.assertEqual(summary_ranges([]), []) # Check if the function returns an empty list for an empty input

    def test_single_element(self): # Test case for a single element list
        self.assertEqual(summary_ranges([1]), []) # Check if the function returns an empty list for a single element input

    def test_one_range(self): # Test case for a list with one range
        self.assertEqual(summary_ranges([1, 2, 3]), ['1->3']) # Check if the function returns the correct range for a consecutive list

    def test_multiple_ranges(self): # Test case for a list with multiple ranges
        self.assertEqual(summary_ranges([0, 1, 2, 4, 5, 7]), ['0->2', '4->5']) #    

    def test_negative_numbers(self): # Test case for a list with negative numbers
        self.assertEqual(summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]), ['110->112', '-5->-4']) # Check if the function returns the correct ranges for a list with negative numbers

    def test_all_disconnected(self): # Test case for a list with all disconnected numbers
        self.assertEqual(summary_ranges([1, 3, 5, 7]), []) # Check if the function returns an empty list for a list with all disconnected numbers

    def test_full_range(self): # Test case for a list with a full range of numbers
        self.assertEqual(summary_ranges(list(range(10))), ['0->9']) # Check if the function returns the correct range for a full range of numbers

    def test_range_at_end(self): # Test case for a list with a range at the end
        self.assertEqual(summary_ranges([3, 5, 6, 7]), ['5->7']) # Check if the function returns the correct range for a list with a range at the end

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
