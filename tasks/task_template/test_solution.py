import unittest # Import the unittest module
from solution import function_name # Import the function from solution.py

class TestFunctionName(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_lfunction_name(self): # Define a test method 
        self.assertEqual(function_name(arguments), expected_result) # Check if the function returns expected result

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
