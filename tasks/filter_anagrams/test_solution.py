import unittest # Import the unittest module
from solution import filter_anagrams # Import the function from solution.py

class TestFilterAnagrams(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_strings(self): # Test case for filtering anagrams from a list of strings
        self.assertEqual(
            list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])),
            ['aabb', 'bbaa']
        )

    def test_partial_anagrams(self): # Test case for filtering anagrams with partial matches
        self.assertEqual(
            list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])),
            ['carer', 'racer']
        )

    def test_no_anagrams(self): # Test case for filtering when there are no anagrams
        self.assertEqual(
            list(filter_anagrams('laser', ['lazing', 'lazy', 'lacer'])),
            []
        )

    def test_lists(self): # Test case for filtering anagrams from a list of lists
        self.assertEqual(
            list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]])),
            [[2, 1], [1, 2]]
        )

    def test_empty_candidates(self): # Test case for filtering when the candidates list is empty
        self.assertEqual(
            list(filter_anagrams('word', [])),
            []
        )

    def test_empty_reference(self): # Test case for filtering when the reference word is empty
        self.assertEqual(
            list(filter_anagrams('', ['', 'a', []])),
            ['']
        )

    def test_tuples(self): # Test case for filtering anagrams from a list of tuples
        self.assertEqual(
            list(filter_anagrams((1, 2), [(2, 1), (1, 1), (1, 2)])),
            [(2, 1), (1, 2)]
        )

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
