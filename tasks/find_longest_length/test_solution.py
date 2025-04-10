import unittest # importing the unittest module
from solution import find_longest_length # importing the function to be tested

class TestFindLongestLength(unittest.TestCase): # Creating a test case class that inherits from unittest.TestCase

    def test_basic_cases(self): # Testing basic cases
        self.assertEqual(find_longest_length('qwearty'), 7) # Test with all unique characters  
        self.assertEqual(find_longest_length('abcdeef'), 5) # Test with some repeating characters 
        self.assertEqual(find_longest_length('jabjcdel'), 7) # Test with a mix of repeating and unique characters 

    def test_edge_cases(self): # Testing edge cases
        self.assertEqual(find_longest_length(''), 0) # Test with an empty string 
        self.assertEqual(find_longest_length('a'), 1) # Test with a single character 
        self.assertEqual(find_longest_length('aaaa'), 1) # Test with all same characters 

    def test_with_repeated_characters(self): # Testing with repeated characters
        self.assertEqual(find_longest_length('abcabac'), 3) # Test with repeated characters 
        self.assertEqual(find_longest_length('aabbccddeeff'), 2) # Test with pairs of repeated characters   

if __name__ == '__main__': # Checking if the script is being run directly
    unittest.main() # Running the tests
