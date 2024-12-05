import random

global lista
lista=[]

def ABC():
    i=0
    while i<8:
        rszam=(random.randint(-100, 859))
        lista.append(rszam)
        i+=1
    i=0
    while i<len(lista):
        if i <len(lista)-1:
            print(f"{lista[i]}",end=";")
        else:
            print(f"{lista[i]}",end=" ")
        i+=1
        
def tizzel_osztahatoak_szama():
    db=0
    for i in lista:
        if i%10==0:
            db+=1
    return db

def konzol_ir():
    kiir=tizzel_osztahatoak_szama()
    print(f"Tízzel osztható számok száma: {kiir}")
    
def fajlba_ir():
    szamok=tizzel_osztahatoak_szama()
    t = open('vegeredmeny.txt', 'w')
    t.write(f"A tizzel osztahtóak száma {szamok}.")
    t.close()


            