import unittest # Import the unittest module
from solution import compose # Import the function from solution.py

class TestComposeFunction(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_basic_functions(self): # Define a test method to test basic function composition
        def add5(x):
            return x + 5
        def mul3(x):
            return x * 3
        composed = compose(mul3, add5) 
        self.assertEqual(composed(1), 18) # Check if the composed function returns the expected result
        self.assertEqual(composed(2), 21) # Check another case
        self.assertEqual(composed(0), 15) # Check the edge case when input is 0

    def test_identity_function(self): # Define a test method to test the identity function
        def identity(x):
            return x
        def square(x):
            return x * x
        composed = compose(square, identity) # Compose square and identity functions
        self.assertEqual(composed(3), 9) # Check if the composed function returns the expected result
        self.assertEqual(composed(5), 25) # Check another case

    def test_string_functions(self): # Define a test method to test string manipulation functions
        def add_exclamation(x): # Function to add an exclamation mark to a string
            return x + "!"
        def to_upper(x): # Function to convert a string to uppercase
            return x.upper() 
        composed = compose(add_exclamation, to_upper) # Compose the two string functions
        self.assertEqual(composed("hello"), "HELLO!") # Check if the composed function returns the expected result

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
