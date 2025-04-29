import unittest # Import the unittest module
from solution import typecheck # Import the function from solution.py

@typecheck # Apply the typecheck decorator to the function.
def greet(name: str, age: int): # Function to greet a person with their name and age.
    return f"Hello, {name}. You are {age} years old." # Return a greeting message.

class TestTypeCheck(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    
    def test_valid_types(self): # Define a test method to test valid types
        self.assertEqual(greet(name="Alice", age=30), "Hello, Alice. You are 30 years old.") # Check if the function returns the expected result

    def test_invalid_name_type(self): # Define a test method to test invalid name type
        with self.assertRaises(TypeError): # Check if TypeError is raised
            greet(name=123, age=30)

    def test_invalid_age_type(self): # Define a test method to test invalid age type
        with self.assertRaises(TypeError): # Check if TypeError is raised
            greet(name="Bob", age="30")

    def test_missing_annotation_ignored(self): # Define a test method to test missing annotation
        @typecheck # Apply the typecheck decorator to the function.
        def foo(x, y: int): # Test function with missing annotation
            return str(x) + str(y) 
        self.assertEqual(foo("A", y=1), "A1") #   

    def test_no_annotations(self): # Define a test method to test no annotations
        @typecheck # Apply the typecheck decorator to the function.
        def identity(x): # Identity function that returns the input value
            return x
        self.assertEqual(identity(42), 42) # Check if the function returns the expected result

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
