
def adatok():
    napok:str=str(input("Hét napja: "))
    oranev:str=str(input("Óra neve: "))
    ertekeles:int=int(input("Értékelés (0-5): "))
    
    while not (0<=ertekeles and ertekeles<=5):
        ertekeles:int=int(input("Értékelés (0-5): "))
        if ertekeles <0:
            print("Az értékelés nem lehet negatív!")
        elif ertekeles>5:
            print("5 pont feletti értékelés nem elfogadható!")
            
    print("Köszönjük az értékelést! ")
    print(f"Összefoglaló: {napok}, {oranev}, {ertekeles}")
    

        
            
    
    