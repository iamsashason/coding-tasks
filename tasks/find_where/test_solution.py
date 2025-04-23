import unittest # Import the unittest module
from solution import find_where # Import the function from solution.py

class TestFindWhere(unittest.TestCase): # Define a test case class that inherits from unittest.TestCase

    def setUp(self): # Set up the test case with a list of books
        self.books = [
            {'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
            {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
            {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
            {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
            {'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
            {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444}
        ]

    def test_find_by_author(self): # Test finding a book by author
        query = {'author': 'Shakespeare'}
        expected = {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}
        result = find_where(self.books, query)
        self.assertEqual(result, expected) # The expected result is the first book by Shakespeare.

    def test_find_by_author_and_year(self): # Test finding a book by author and year
        query = {'author': 'Shakespeare', 'year': 1611}
        expected = {'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611}
        result = find_where(self.books, query)
        self.assertEqual(result, expected) # The expected result is the first book by Shakespeare from 1611.

    def test_find_by_title(self): # Test finding a book by title
        query = {'title': 'Happy Foo'}
        expected = {'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444}
        result = find_where(self.books, query)
        self.assertEqual(result, expected) # The expected result is the book with title 'Happy Foo'.

    def test_no_match(self): # Test finding a book with no match
        query = {'author': 'Unknown'}
        result = find_where(self.books, query)
        self.assertIsNone(result) # No book should match this query.

    def test_empty_query(self): # Test finding a book with an empty query
        query = {}
        result = find_where(self.books, query)
        self.assertEqual(result, self.books[0])  # The first book should be returned as it matches all criteria (empty query).

if __name__ == '__main__': # Check if the script is being run directly (not imported as a module).
    unittest.main() # Run the test case class using unittest's test runner.
