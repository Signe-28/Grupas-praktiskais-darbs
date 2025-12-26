import borrowing_manager
import book_manager

# Izvēlas darbību ko grib veikt
pareizs_input = False
while not pareizs_input:
    try:
        izveletais_skaitlis = int(input("Izvēlies darbību (ievadi skaitli): \n1. Pievienot/atjaunināt grāmatu\n2. Apskatīt visas grāmatas\n3. Aizņemties/atgriezt grāmatu\n4. Meklēt grāmatu\n5. Apskatīt Top 5 sarakstus"))
        if 0 < izveletais_skaitlis < 6:
            pareizs_input = True
        else:
            print("Ievadi atbilstošu skaitli!")
    except:
        print("Ievadi pareiza tipa vērtību! (integer)")

# Izvēlas atbilstošo funkciju
match izveletais_skaitlis:
    case 1:
        pass
    case 2:
        pass
    case 3: 
        borrowing_manager.borrow_return_book()
    case 4:
        borrowing_manager.search_book()
    case 5:
        borrowing_manager.top_5_least_borrowed()
        # Jāpievieno pārējās funkcijas
    case _:
        print("Error 404!")