import unittest # Import the unittest module
from collections import Counter # Importing the Counter class from the collections module to count hashable objects.
from solution import visualize # Import the function from solution.py

class TestVisualizeFunction(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic_visualization(self): # Test the basic functionality of the visualize function
        coins = [1, 2, 1, 3, 2, 1]
        expected_output = (
            "$\n"
            "$ $\n"
            "$ $ $\n"
            "1 2 3"
        )
        self.assertEqual(visualize(coins), expected_output) # Check if the output matches the expected output

    def test_custom_bar_char(self): # Test the functionality with a custom bar character
        coins = [5, 5, 10]
        expected_output = (
            "*\n"
            "* *\n"
            "5 10"
        )
        self.assertEqual(visualize(coins, bar_char='*'), expected_output) # Check if the output matches the expected output

    def test_single_denomination(self): # Test the functionality with a single denomination
        coins = [100, 100, 100]
        expected_output = (
            "$\n"
            "$\n"
            "$\n"
            "100"
        )
        self.assertEqual(visualize(coins), expected_output) # Check if the output matches the expected output

    def test_order_of_appearance(self): # Test the order of appearance of denominations
        coins = [10, 1, 10, 5, 1]
        expected_output = (
            "$ $\n"
            "$ $ $\n"
            "10 1 5"
        )
        self.assertEqual(visualize(coins), expected_output) # Check if the output matches the expected output

    def test_empty_list_raises(self): # Test that an empty list raises a ValueError
        with self.assertRaises(ValueError): # Check if a ValueError is raised
            visualize([]) 

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
