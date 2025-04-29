import unittest # Import the unittest module
from solution import typecheck, typecheck_all # Import the functions from solution.py

class TestTypecheckAll(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_correct_usage(self): # Define a test method to test correct usage of the typecheck_all decorator
        @typecheck_all # Apply the typecheck_all decorator to the function 
        def greet(name: str, age: int, city: str): # Function to greet a person with their name, age, and city
            return f"{name} ({age}), from {city}" # Return a formatted string with the person's details
        self.assertEqual(greet(name="Alice", age=30, city="Paris"), "Alice (30), from Paris") # Check if the function returns the expected result

    def test_single_type_error(self): # Define a test method to test a single type error
        @typecheck_all # Apply the typecheck_all decorator to the function
        def greet(name: str, age: int, city: str): # Function to greet a person with their name, age, and city
            return f"{name} ({age}), from {city}" # Return a formatted string with the person's details
        with self.assertRaises(TypeError) as context: # Check if a TypeError is raised
            greet(name="Bob", age="thirty", city="London") # Call the function with incorrect argument types
        self.assertIn("Argument 'age' should be of type", str(context.exception)) # Check if the error message contains the expected text

    def test_multiple_type_errors(self): # Define a test method to test multiple type errors
        @typecheck_all # Apply the typecheck_all decorator to the function
        def greet(name: str, age: int, city: str): # Function to greet a person with their name, age, and city
            return f"{name} ({age}), from {city}" # Return a formatted string with the person's details
        with self.assertRaises(TypeError) as context: # Check if a TypeError is raised
            greet(name=123, age="old", city=42) # Call the function with incorrect argument types
        error_message = str(context.exception) # Get the error message from the exception
        self.assertIn("Argument 'name' should be of type", error_message) # Check if the error message contains the expected text
        self.assertIn("Argument 'age' should be of type", error_message) # Check if the error message contains the expected text
        self.assertIn("Argument 'city' should be of type", error_message) # Check if the error message contains the expected text

    def test_missing_annotation_ignored(self): # Define a test method to test missing annotation
        @typecheck_all # Apply the typecheck_all decorator to the function
        def foo(x, y: int): # Function to concatenate a string and an integer
            return f"{x}{y}" # Return a formatted string with the concatenated values
        self.assertEqual(foo("A", y=1), "A1") # Check if the function returns the expected result
        with self.assertRaises(TypeError): # Check if a TypeError is raised
            foo("A", y="B") # Call the function with incorrect argument types

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
