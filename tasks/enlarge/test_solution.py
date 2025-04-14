import unittest # Import the unittest module
from solution import enlarge # Import the function from solution.py

class TestEnlarge(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_enlarge(self): # Define a test method to test the enlarge function
        frame = [
            "****",
            "*  *",
            "****"
        ] # Define a sample input frame
        enlarged = enlarge(frame) # Call the enlarge function with the sample input
        expected = [
            "********",
            "********",
            "**    **",
            "**    **",
            "********",
            "********"
        ] # Define the expected output after enlarging the input frame
        self.assertEqual(enlarged, expected) # Assert that the enlarged output matches the expected output

    def test_single_line(self): # Define a test method to test the enlarge function with a single line input
        frame = [
            "****"
        ]  # Define a single line input frame
        enlarged = enlarge(frame)
        expected = [
            "********",
            "********"
        ] # Define the expected output after enlarging the single line input
        self.assertEqual(enlarged, expected) # Assert that the enlarged output matches the expected output

    def test_single_column(self): # Define a test method to test the enlarge function with a single column input
        frame = [
            "*",
            " ",
            "*"
        ] # Define a single column input frame
        enlarged = enlarge(frame)
        expected = [
            "**",
            "**",
            "  ",
            "  ",
            "**",
            "**"
        ] # Define the expected output after enlarging the single column input
        self.assertEqual(enlarged, expected) # Assert that the enlarged output matches the expected output

    def test_empty(self): # Define a test method to test the enlarge function with an empty input
        frame = [] # Define an empty input frame
        enlarged = enlarge(frame) # Call the enlarge function with the empty input
        expected = [] # Define the expected output after enlarging the empty input
        self.assertEqual(enlarged, expected) # Assert that the enlarged output matches the expected output

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
