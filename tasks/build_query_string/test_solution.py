import unittest # Import the unittest module
from solution import build_query_string # Import the function from solution.py

class TestBuildQueryString(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic_case(self): # Test case for a basic scenario
        params = {'per': 10, 'page': 1}
        expected = 'page=1&per=10'
        self.assertEqual(build_query_string(params), expected)

    def test_single_param(self): # Test case for a single parameter
        params = {'limit': 100}
        expected = 'limit=100'
        self.assertEqual(build_query_string(params), expected)

    def test_multiple_params_unsorted(self): # Test case for multiple parameters in unsorted order
        params = {'z': 9, 'a': 1, 'm': 5}
        expected = 'a=1&m=5&z=9'
        self.assertEqual(build_query_string(params), expected)

    def test_empty_dict(self): # Test case for an empty dictionary
        params = {}
        expected = ''
        self.assertEqual(build_query_string(params), expected)

    def test_string_values(self): # Test case for string values in the dictionary
        params = {'b': 'beta', 'a': 'alpha'}
        expected = 'a=alpha&b=beta'
        self.assertEqual(build_query_string(params), expected)

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
