import unittest # Import the unittest module
from solution import length_of_last_word # Import the function from solution.py

class TestLengthOfLastWord(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_length_of_last_word_0(self): # Define a test method for n = ''
        self.assertEqual(length_of_last_word(''), 0) # Check if the function returns 0 for an empty string

    def test_length_of_last_word_0(self): # Define a test method for n = 'man in Black'
        self.assertEqual(length_of_last_word('man in Black'), 5) # Check if the function returns 5 

    def test_length_of_last_word_0(self): # Define a test method for n = 'hello, world!'
        self.assertEqual(length_of_last_word('hello, world!'), 6) # Check if the function returns 6 
    
    def test_length_of_last_word_0(self): # Define a test method for n = 'hello\t\nworld'
        self.assertEqual(length_of_last_word('hello\t\nworld'), 5) # Check if the function returns 5 

    def test_length_of_last_word_0(self): # Define a test method for n = 'hello world'
        self.assertEqual(length_of_last_word("hello world"), 5) # Check if the function returns 5 

    def test_length_of_last_word_0(self): # Define a test method for n = 'Python is awesome '
        self.assertEqual(length_of_last_word("Python is awesome "), 7) # Check if the function returns 7

    def test_length_of_last_word_0(self): # Define a test method for n = "one\ttwo\nthree "
        self.assertEqual(length_of_last_word("one\ttwo\nthree "), 5) # Check if the function returns 5

    def test_length_of_last_word_0(self): # Define a test method for n = "   "
        self.assertEqual(length_of_last_word("   "), 0) # Check if the function returns 0

    def test_length_of_last_word_0(self): # Define a test method for n = ""
        self.assertEqual(length_of_last_word(""), 0) # Check if the function returns 0

    def test_length_of_last_word_0(self): # Define a test method for n = "hello world"
        self.assertEqual(length_of_last_word("hello world"), 5) # Check if the function returns 5

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.

   