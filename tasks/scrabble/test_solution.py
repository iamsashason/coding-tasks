import unittest # Import the unittest module
from collections import Counter # Import Counter from collections for counting hashable objects
from solution import scrabble # Import the function from solution.py

class TestScrabble(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_exact_match(self): # Test case for exact match
        self.assertTrue(scrabble("reaction", "action"))

    def test_extra_letters(self): # Test case for extra letters
        self.assertTrue(scrabble("reactionxyz", "reaction"))

    def test_insufficient_letters(self): # Test case for insufficient letters
        self.assertFalse(scrabble("reactio", "reaction"))  # missing 'n'

    def test_case_insensitivity(self): # Test case for case insensitivity
        self.assertTrue(scrabble("ReAcTiOn", "ACTION"))  # different case

    def test_repeated_letters(self): # Test case for repeated letters
        self.assertFalse(scrabble("reactio", "actionn"))  # need two 'n's, only have one

    def test_empty_word(self): # Test case for empty word
        self.assertTrue(scrabble("anything", ""))  # empty word is always buildable

    def test_empty_letters(self): # Test case for empty letters
        self.assertFalse(scrabble("", "anything"))  # can't build anything with no letters

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
