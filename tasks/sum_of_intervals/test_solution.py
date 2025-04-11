import unittest # Import the unittest module
from solution import sum_of_intervals # Import the sum_of_intervals function from solution.py

class TestSumOfIntervals(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase
    def test_sum_of_intervals_0(self): # Define a test method for n = [[1, 1]]
        self.assertEqual(sum_of_intervals([1, 1]), 0)

    def test_sum_of_intervals_1(self): # Define a test method for n = [[1, 2], [50, 100], [60, 70]]
        self.assertEqual(sum_of_intervals([1, 2], [50, 100], [60, 70]), 51)

    def test_sum_of_intervals_2(self): # Define a test method for n = [[1, 2], [5, 10]]
        self.assertEqual(sum_of_intervals([1, 2], [5, 10]), 6)

    def test_sum_of_intervals_3(self): # Define a test method for n = [[4, 7], [5, 10], [50, 100], [40, 110]]
        self.assertEqual(sum_of_intervals([4, 7], [5, 10], [50, 100], [40, 110]), 76)


if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
