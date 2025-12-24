import json


class BookManager:
    def __init__(self, filepath):
        self._filepath = filepath

    def _load_books(self):
        with open(self._filepath, "r") as f:
            books = json.load(f)
        return books

    def print_books(self):
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

    def _create_new_book(self):
        while True:
            try:
                name = input("Book name: ")
                author = input("Book author: ")

                while True:
                    price = float(input("Book price: "))
                    if (price < 0):
                        print("Price cannot be negative")
                        continue
                    break

                while True:
                    in_storage = int(input("Book amount in storage: "))
                    if (in_storage < 0):
                        print("Amount cannot be negative")
                        continue
                    break

                book = {"name": name, "author": author, "price": price,
                        "inStorage": in_storage}

                return book

            except ValueError:
                print("Please enter a valid number")

    def _add_book(self):
        books = self._load_books()
        new_book = self._create_new_book()
        new_book["borrowed"] = 0
        books.append(new_book)
        with open(self._filepath, "w") as f:
            json.dump(books, f)

    def _update_book(self):
        books = self._load_books()
        is_book_found = False
        name = input("Book to update: ").lower()

        for book in books:
            if book["name"].lower() == name:
                new_book = self._create_new_book()
                while True:
                    try:
                        new_book["borrowed"] = int(
                            input("Amount of books borrowed: "))
                        if (new_book["borrowed"] < 0):
                            print("Amount cannot be negative")
                            continue
                        break
                    except ValueError:
                        print("Please enter an integer")
                book.update(new_book)
                is_book_found = True
                break

        if not is_book_found:
            print("No book was found")
        else:
            with open(self._filepath, "w") as f:
                json.dump(books, f)

    def add_update_book(self):
        while True:
            try:
                choice = int(input("Add (1)\nUpdate (2)\nExit (3)\n"))
                match choice:
                    case 1:
                        self._add_book()
                        return
                    case 2:
                        self._update_book()
                        return
                    case 3:
                        return
                    case _:
                        print("Invalid choice")
            except ValueError:
                print("Please enter an integer")
