import json

### GRĀMATU AIZŅEMŠANĀS UN ATGRIEŠANA
def borrow_return_book():
    
    #input nosaukumam un skaitam
    correct_input = False
    while not correct_input:
        try:
            name = str(input("Grāmatas nosaukums: ")).strip().lower()
            quantity = int(input("Grāmatu skaits, ko vēlies aizņemties: "))
            borrow_or_return = int(input("Vai vēlie aizņemties(1) vai atgriezt(2) grāmatu? "))
            if borrow_or_return == 1 or borrow_or_return == 2 and quantity >= 0:
                correct_input = True
            else:
                print("Ievadi pareizu vērtību!")
        except:
            print("Ievadi pareiza tipa vērtības lūdzu!")
    
    # Nolasa info no faila
    with open("library_data.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Nomaina skaitu
    book_found = False
    for element in data:
        if element["name"].strip().lower() == name:
            if borrow_or_return == 1 and element["inStorage"] - quantity >= 0: 
                element["inStorage"] -= quantity
                element["borrowed"] += quantity
                book_found = True
            if borrow_or_return == 2 and element["borrowed"] - quantity >= 0:
                element["borrowed"] -= quantity
                element["inStorage"] += quantity
                book_found = True
    if not book_found:
        print("Šāda grāmata nav bibliotēkā vai skaits pārāk liels!")
    
    # Atjauno info failā
    if book_found:
        with open("library_data.json", mode="w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


### GRĀMATU MEKLĒŠANA
def search_book():
         
    #input nosaukumam vai autoram
    correct_input = False
    while not correct_input:
        try:
            meklesanas_nosacijumi = int(input("Pēc kāda parametra jāmeklē grāmata?\n1. Pēc grāmatas nosaukuma\n2. Pēc autora"))
            if meklesanas_nosacijumi == 1:
                name = str(input("Grāmatas nosaukums: ")).strip().lower()
                correct_input = True
            elif meklesanas_nosacijumi == 2:
                author = str(input("Autora vārds: ")).strip().lower()
                correct_input = True
            else:
                print("Ievadi pareizu vērtību!")
        except:
            print("Ievai pareiza tipa vērtības lūdzu!")
    
    # Nolasa info no faila
    with open("library_data.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Grāmatas meklēšana
    book_found = []
    for element in data:
        if meklesanas_nosacijumi == 1 and element["name"].strip().lower() == name:
            book_found.append(element)
        elif meklesanas_nosacijumi == 2 and element["author"].strip().lower() == author:
            book_found.append(element)
        
    # Grāmatu izprintēšana
    if book_found:
        for book in book_found:
            print(book)
    else:
        print("Grāmata netika atrasta")


### TOP 5 VISMAZĀK IZSNIEGTĀS GRĀMATAS
def top_5_least_borrowed():
      
    with open("library_data.json", mode="r", encoding="utf-8") as f:
        data = json.load(f)
        
    sorted_books = sorted(data, key=lambda x: x["borrowed"])
    top_5 = sorted_books[:5]
    for i, book in enumerate(top_5, start=1):
        print(f"{i}. {book['name']} - {book['borrowed']} aizņemts")                
                