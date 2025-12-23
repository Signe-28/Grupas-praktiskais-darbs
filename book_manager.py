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

    def _create_new_book(self):
        while True:
            try:
                name = input("Book name: ")
                author = input("Book author: ")
                price = float(input("Book price: "))
                in_storage = int(input("Book amount in storage: "))

                book = {"name": name, "author": author, "price": price,
                        "inStorage": in_storage}

                return book

            except ValueError:
                print("Invalid number")

    def add_book(self):
        try:
            books = self._load_books()
            new_book = self._create_new_book()
            new_book["borrowed"] = 0
            books.append(new_book)
            with open(self._filepath, "w") as f:
                json.dump(books, f)

        except Exception as e:
            print(f"Error adding book: {e}")

    def update_book(self):
        try:
            books = self._load_books()
            is_book_found = False
            name = input("Book to update").lower()

            for book in books:
                if book["name"].lower() == name:
                    new_book = self._create_new_book()
                    new_book["borrowed"] = int(
                        input("Amount of books borrowed: "))
                    book.update(new_book)
                    is_book_found = True
                    break

            if not is_book_found:
                print("No book was found")
            else:
                with open(self._filepath, "w") as f:
                    json.dump(books, f)

        except Exception as e:
            print(f"Error updating book: {e}")

