import unittest # Import the unittest module
from solution import gen_diff # Import the function from solution.py

class TestGenDiff(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_basic_diff(self): # Define a test method to test the basic functionality
        d1 = {"one": "eon", "two": "two", "four": True}
        d2 = {"two": "own", "zero": 4, "four": True}
        expected = {
            "one": "deleted",
            "two": "changed",
            "four": "unchanged",
            "zero": "added"
        }
        self.assertEqual(gen_diff(d1, d2), expected)

    def test_all_unchanged(self): # Define a test method to test when all values are unchanged
        d1 = {"a": 1, "b": 2}
        d2 = {"a": 1, "b": 2}
        expected = {"a": "unchanged", "b": "unchanged"}
        self.assertEqual(gen_diff(d1, d2), expected)

    def test_all_added(self): # Define a test method to test when all values are added
        d1 = {}
        d2 = {"x": 10, "y": 20}
        expected = {"x": "added", "y": "added"}
        self.assertEqual(gen_diff(d1, d2), expected)

    def test_all_deleted(self): # Define a test method to test when all values are deleted
        d1 = {"x": 10, "y": 20}
        d2 = {}
        expected = {"x": "deleted", "y": "deleted"}
        self.assertEqual(gen_diff(d1, d2), expected)

    def test_changed_and_added(self): # Define a test method to test when some values are changed and some are added
        d1 = {"a": 1}
        d2 = {"a": 2, "b": 3}
        expected = {"a": "changed", "b": "added"}
        self.assertEqual(gen_diff(d1, d2), expected)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
