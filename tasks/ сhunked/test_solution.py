import unittest # importing the unittest module
from solution import chunked # importing the function to be tested

class TestChunkedFunction(unittest.TestCase): # creating a test case class that inherits from unittest.TestCase

    def test_basic_cases(self): # testing basic cases
        self.assertEqual(chunked(2, ['a','b','c','d']), [['a','b'],['c','d']]) # test with a list of characters
        self.assertEqual(chunked(3, ['a','b','c','d']), [['a','b','c'],['d']]) # test with a list of characters
        self.assertEqual(chunked(3,'foobar'), ['foo','bar']) # test with a string
        self.assertEqual(chunked(10, (42,)), [(42,)]) # test with a tuple
        self.assertEqual(chunked(2, 'abcdef'), ['ab', 'cd', 'ef']) # test with a string
        self.assertEqual(chunked(1, 'abc'), ['a', 'b', 'c']) # test with a string
        self.assertEqual(chunked(2, 'a'), ['a']) # test with a string

if __name__ == '__main__': # Checking if the script is being run directly
    unittest.main() # Running the tests