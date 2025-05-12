import unittest # Import the unittest module
from solution import rgb2hex # Import the function from solution.py

class TestRgb2Hex(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase.
    
    def test_rgb2hex(self): # Test case for the rgb2hex function.
        self.assertEqual(rgb2hex(36, 171, 0), '#24ab00') # Test method to check if the function returns the expected output.
        self.assertEqual(rgb2hex(0, 0, 0), '#000000')  # Black color
        self.assertEqual(rgb2hex(255, 255, 255), '#ffffff')  # White color
        self.assertEqual(rgb2hex(255, 0, 0), '#ff0000') # Red color 
        self.assertEqual(rgb2hex(0, 255, 0), '#00ff00') # Green color  
        self.assertEqual(rgb2hex(0, 0, 255), '#0000ff') # Blue color  
        self.assertEqual(rgb2hex(10, 100, 200), '#0a64c8')  # Test with mixed values
        self.assertEqual(rgb2hex(123, 45, 67), '#7b2d43')  # Test with mixed values

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
