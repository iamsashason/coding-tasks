import unittest # Import the unittest module
from solution import compare_version # Import the function from solution.py

class TestCompareVersion(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_equal_versions(self): # Test case for equal versions
        self.assertEqual(compare_version("1.0", "1.0"), 0) # Check if the function returns 0 for equal versions
        self.assertEqual(compare_version("0.0", "0.0"), 0) # Check if the function returns 0 for equal versions

    def test_major_greater(self): # Test case for major version greater
        self.assertEqual(compare_version("2.0", "1.9"), 1) # Check if the function returns 1 for major version greater
        self.assertEqual(compare_version("3.5", "2.9"), 1) # Check if the function returns 1 for major version greater

    def test_major_less(self): # Test case for major version less
        self.assertEqual(compare_version("1.2", "2.0"), -1) # Check if the function returns -1 for major version less
        self.assertEqual(compare_version("0.9", "1.0"), -1) # Check if the function returns -1 for major version less

    def test_minor_greater(self): # Test case for minor version greater
        self.assertEqual(compare_version("1.2", "1.1"), 1) # Check if the function returns 1 for minor version greater
        self.assertEqual(compare_version("0.10", "0.3"), 1) # Check if the function returns 1 for minor version greater

    def test_minor_less(self): # Test case for minor version less
        self.assertEqual(compare_version("2.3", "2.4"), -1) # Check if the function returns -1 for minor version less
        self.assertEqual(compare_version("5.0", "5.1"), -1) # Check if the function returns -1 for minor version less

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
