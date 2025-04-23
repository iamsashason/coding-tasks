Implement a find_where function that takes a list of books and a search query as input and returns the first book that matches the query. Each book in the list is a dictionary containing its parameters, and the search query is also a dictionary with parameters. If there are no matches, the function should return None.

Example:
>>> books = [
{'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111}, {'title': 'Cymbeline', 'author': 'Shakespeare', "year': 1611}, {'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611}, {'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222}, {'title': 'Still foooing', 'author': 'FooBar', 'year': 333}, {'title': "Happy Foo', 'author': 'FooBar", 'year': 4444},
]
>>> find_where(books, {'author': 'Shakespeare',  'year': 1611})

{'title': 'Cymbeline', 'author':'Shakespeare', year': 1611}
