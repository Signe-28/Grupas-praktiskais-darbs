import borrowing_manager
from book_manager import BookManager

book_manager = BookManager("library_data.json")

while True:
    # Izvēlas darbību ko grib veikt
    pareizs_input = False
    while not pareizs_input:
        try:
            print("-" * 100)
            izveletais_skaitlis = int(input(
                "Izvēlies darbību (ievadi skaitli): \nPievienot/atjaunināt grāmatu (1)\nApskatīt visas grāmatas (2)\nAizņemties/atgriezt grāmatu (3)\nMeklēt grāmatu (4)\nApskatīt Top 5 sarakstus (5)\n"))
            if 0 < izveletais_skaitlis < 6:
                pareizs_input = True
            else:
                print("-" * 100)
                print("Ievadi atbilstošu skaitli!")
        except:
            print("-" * 100)
            print("Ievadi pareiza tipa vērtību! (integer)")

    # Izvēlas atbilstošo funkciju
    match izveletais_skaitlis:
        case 1:
            book_manager.add_update_book()
        case 2:
            book_manager.print_all_books()
        case 3:
            borrowing_manager.borrow_return_book()
        case 4:
            borrowing_manager.search_book()
        case 5:
            borrowing_manager.top_5_least_borrowed()
            book_manager.top_5_borrowed()
            book_manager.top_5_expensive()
        case _:
            print("Error 404!")
