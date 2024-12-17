varosok = ["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]

while True:
    city = input("Adj meg egy várost: ")
    
    if city in varosok:
        index = varosok.index(city)
        if index < len(varosok) - 1:  
            print(f"A következő város: {varosok[index + 1]}")
        else:  
            print("Nincs következő város.")
    else:
        varosok.append(city)  
        print(f"{city} hozzáadva a listához.")