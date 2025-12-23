import json


class BookManager:
    def __init__(self, filepath):
        self.__filepath = filepath

    def print_books(self):
        with open(self.filepath, "r") as f:
            books = json.load(f)
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
