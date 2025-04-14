import unittest # Import the unittest module
from solution import rpn_calc # Import the function from solution.py

class TestRpnCalc(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_basic_operations(self): # Define a test method to check basic operations
        self.assertEqual(rpn_calc([1, 2, '+']), 3) # Check addition
        self.assertEqual(rpn_calc([5, 3, '-']), 2) # Check subtraction
        self.assertEqual(rpn_calc([4, 3, '*']), 12) # Check multiplication
        self.assertEqual(rpn_calc([8, 2, '/']), 4) # Check division

    def test_combined_expression(self):
        self.assertEqual(rpn_calc([1, 2, '+', 4, '*', 3, '+']), 15)
        self.assertEqual(rpn_calc([7, 2, 3, '*', '-']), 1)

    def test_with_floats(self):
        self.assertAlmostEqual(rpn_calc([3.5, 2, '*']), 7.0)
        self.assertAlmostEqual(rpn_calc([10, 4, '/', 2, '*']), 5.0)

    def test_single_element(self):
        self.assertEqual(rpn_calc([42]), 42)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            rpn_calc([5, 0, '/'])

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.

   