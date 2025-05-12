import unittest # Import the unittest module for creating unit tests.
from solution import enlarge2 # Import the enlarge2 function from the solution module.

class TestEnlarge(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase.
    def test_enlarge_simple_image(self): # Test case for a simple image.
        original = [' * ', '  *', '***'] # Original image represented as a list of strings.
        expected = [
            '  **  ',
            '  **  ',
            '    **',
            '    **',
            '******',
            '******'
        ] # Expected enlarged image.
        self.assertEqual(enlarge2(original), expected) # Assert that the enlarged image matches the expected output.

    def test_enlarge_empty_image(self): # Test case for an empty image.
        self.assertEqual(enlarge2([]), []) # Assert that enlarging an empty image returns an empty list.

    def test_enlarge_single_pixel(self): # Test case for a single pixel image.
        original = ['#'] # Original image represented as a list of strings.
        expected = ['##', '##'] # Expected enlarged image.
        self.assertEqual(enlarge2(original), expected) # Assert that the enlarged image matches the expected output.

    def test_enlarge_uniform_image(self): # Test case for a uniform image.
        original = ['aa', 'aa'] # Original image represented as a list of strings.
        expected = ['aaaa', 'aaaa', 'aaaa', 'aaaa'] # Expected enlarged image.
        self.assertEqual(enlarge2(original), expected) # Assert that the enlarged image matches the expected output.

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
