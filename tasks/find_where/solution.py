#!/usr/bin/env python3 # Shebang line to specify the interpreter for executing the script.

def find_where(books, query):
    for book in books:
        if all(book.get(key) == value for key, value in query.items()):
            return book
    return None

def main(): # Main function to execute the program.
    books = [
        {"title": "Book A", "author": "Author A", "year": 2000},
        {"title": "Book B", "author": "Author B", "year": 2001},
        {"title": "Book C", "author": "Author C", "year": 2002},
    ]
    query = {"author": "Author B", "year": 2001}
    print(find_where(books, query)) # Prints the result of the find_where function with a query for books by "Author A" published in 2000.

if __name__ == "__main__": # Checks if the script is being run directly (not imported as a module).
    main() # If the script is run directly (not imported as a module), calls the main function to execute the program.