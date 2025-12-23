import json


class BookManager:
    def __init__(self, filepath):
        self._filepath = filepath

    def _load_books(self):
        try:
            with open(self._filepath, "r") as f:
                books = json.load(f)
            return books
        
        except Exception as e:
            print(f"Error loading books: {e}")

    def print_books(self):
        try:
            books = self._load_books()
            if not books:
                print("No books found")
            else:
                for book in books:
                    print("-" * 100)
                    print(f"Name: {book["name"]}")
                    print(f"Author: {book["author"]}")
                    print(f"Price: {book["price"]}")
                    print(f"In storage: {book["inStorage"]}")
                    print(f"Borrowed: {book["borrowed"]}")
        except Exception as e:
            print(f"Error printing books: {e}")