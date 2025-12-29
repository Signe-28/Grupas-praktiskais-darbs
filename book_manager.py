import json


class BookManager:
    def __init__(self, filepath):
        self._filepath = filepath

    def _load_books(self):
        with open(self._filepath, "r", encoding="utf-8") as f:
            books = json.load(f)
        return books

    def _print_book_list(self, books):
        if not books:
            print("Grāmatas nav atrastas")
        else:
            for book in books:
                print("-" * 100)
                print(f'Nosaukums: {book["name"]}')
                print(f'Autors: {book["author"]}')
                print(f'Cena: {book["price"]}')
                print(f'Uz vietas: {book["inStorage"]}')
                print(f'Aizdotas: {book["borrowed"]}')

    def print_all_books(self):
        books = self._load_books()
        self._print_book_list(books)

    def _create_new_book(self):
        while True:
            try:
                name = input("Grāmatas nosaukums: ")
                author = input("Grāmatas autors: ")

                while True:
                    price = float(input("Grāmatas cena: "))
                    if (price < 0):
                        print("Cena nevar būt negatīva")
                        continue
                    break

                while True:
                    in_storage = int(input("Grāmatu skaits noliktavā: "))
                    if (in_storage < 0):
                        print("Skaits nevar būt negatīvs")
                        continue
                    break

                book = {"name": name, "author": author, "price": price,
                        "inStorage": in_storage}

                return book

            except ValueError:
                print("Lūdzu, ievadiet derīgu skaitli")

    def _add_book(self):
        books = self._load_books()
        new_book = self._create_new_book()
        new_book["borrowed"] = 0
        books.append(new_book)
        with open(self._filepath, "w", encoding="utf-8") as f:
            json.dump(books, f, indent=4)

    def _update_book(self):
        books = self._load_books()
        is_book_found = False
        name = input("Grāmata, kuru atjaunināt: ").lower()

        for book in books:
            if book["name"].lower() == name:
                new_book = self._create_new_book()
                while True:
                    try:
                        new_book["borrowed"] = int(
                            input("Aizņemto grāmatu skaits: "))
                        if (new_book["borrowed"] < 0):
                            print("Skaits nevar būt negatīvs")
                            continue
                        break
                    except ValueError:
                        print("Lūdzu, ievadiet veselu skaitli")
                book.update(new_book)
                is_book_found = True
                break

        if not is_book_found:
            print("Grāmata netika atrasta")
        else:
            with open(self._filepath, "w", encoding="utf-8") as f:
                json.dump(books, f, indent=4)

    def add_update_book(self):
        while True:
            try:
                choice = int(
                    input("Pievienot (1)\nAtjaunināt (2)\nIziet (3)\n"))
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
                        print("Nederīga izvēle")
            except ValueError:
                print("Lūdzu, ievadiet veselu skaitli")

    def _top_5_by_key(self, key):
        books = self._load_books()

        top_5_books = []

        try:
            for _ in range(5):
                top_book = max(
                    books, key=lambda book: book[key])
                if top_book:
                    top_5_books.append(top_book)
                    books.remove(top_book)
                else:
                    break

            return top_5_books
        except ValueError:
            return []

    def top_5_borrowed(self):
        top_5_borrowed = self._top_5_by_key("borrowed")
        print("-"*100)
        print("Top 5 aizņemtākās grāmatas:")
        self._print_book_list(top_5_borrowed)

    def top_5_expensive(self):
        top_5_expensive = self._top_5_by_key("price")
        print("-"*100)
        print("Top 5 dārgākās grāmatas:")
        self._print_book_list(top_5_expensive)
