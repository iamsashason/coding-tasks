import unittest # Import the unittest module
from solution import merged # Import the function from solution.py

class TestMergedFunction(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_empty_input(self): # Test case for empty input
        self.assertEqual(merged(), {})

    def test_single_dict(self): # Test case for a single dictionary
        self.assertEqual(merged({'a': 1, 'b': 2}), {'a': {1}, 'b': {2}})

    def test_multiple_dicts_no_overlap(self): # Test case for multiple dictionaries with no overlapping keys
        result = merged({'a': 1}, {'b': 2}, {'c': 3})
        expected = {'a': {1}, 'b': {2}, 'c': {3}}
        self.assertEqual(result, expected)

    def test_multiple_dicts_with_overlap(self): # Test case for multiple dictionaries with overlapping keys
        result = merged({'a': 1, 'b': 2}, {'b': 10, 'c': 100})
        expected = {'a': {1}, 'b': {2, 10}, 'c': {100}}
        self.assertEqual(result, expected)

    def test_duplicate_values(self): # Test case for duplicate values in the same dictionary
        result = merged({'x': 5}, {'x': 5}, {'x': 5})
        expected = {'x': {5}}
        self.assertEqual(result, expected)

    def test_different_types(self): # Test case for different types of values
        result = merged({'k': 1}, {'k': '1'}, {'k': (1,)})
        expected = {'k': {1, '1', (1,)}}
        self.assertEqual(result, expected)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
