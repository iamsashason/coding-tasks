import unittest # Import the unittest module
from unittest.mock import patch # Import patch from unittest.mock to mock inputs
from collections import OrderedDict # Import OrderedDict from collections module
from solution import asks, interactive, asks_registry # Import the function from solution.py

class TestInteractiveDSL(unittest.TestCase): # Define a test case class inheriting from unittest.TestCase
    def test_interactive_addition(self): # Test case for the interactive addition function
        @interactive("Test Calculator") # Decorate the function to make it interactive with a title
        @asks('a', 'Enter A: ') # Register the first argument 'a' with a prompt
        @asks('b', 'Enter B: ') # Register the second argument 'b' with a prompt
        def add(a, b): # Define the addition function
            return str(int(a) + int(b)) # Return the sum of a and b as a string

        with patch('builtins.input', side_effect=['3', '5']), \
             patch('builtins.print') as mock_print: # Mock the input and print functions

            add()  # Call the add function to start the interactive calculator

        mock_print.assert_any_call("Test Calculator") # Check if the title is printed
        mock_print.assert_any_call("8") # Check if the result is printed

    def test_prompt_order(self): # Test case for the order of prompts
        @asks('first', 'Prompt 1: ') # Register the first argument 'first' with a prompt
        @asks('second', 'Prompt 2: ') # Register the second argument 'second' with a prompt
        def dummy(first, second): pass # Define a dummy function

        prompts = list(asks_registry[dummy].items()) # Get the registered prompts for the dummy function
        self.assertEqual(prompts[0][0], 'second') # Check if the first prompt is 'second'
        self.assertEqual(prompts[1][0], 'first') # Check if the second prompt is 'first'

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
