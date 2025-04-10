import unittest # Import the unittest module
from solution import triangle # Import the triangle function from solution.py

class TestTriangle(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def test_triangle_0(self): # Define a test method for n = 0
        self.assertEqual(triangle(0), [1])

    def test_triangle_1(self): # Define a test method for n = 1
        self.assertEqual(triangle(1), [1, 1])

    def test_triangle_2(self): # Define a test method for n = 2
        self.assertEqual(triangle(2), [1, 2, 1])

    def test_triangle_3(self): # Define a test method for n = 3
        self.assertEqual(triangle(3), [1, 3, 3, 1])

    def test_triangle_4(self): # Define a test method for n = 4
        self.assertEqual(triangle(4), [1, 4, 6, 4, 1])

    def test_triangle_5(self): # Define a test method for n = 5
        self.assertEqual(triangle(5), [1, 5, 10, 10, 5, 1])

if __name__ == '__main__':
    unittest.main()
