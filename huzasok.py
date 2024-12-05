from hatoslotto import Hatoslotto

def beolvas(huzasok.txt,lotto_lista=[]):
    lottok=[]
    fajl=open('huzasok.txt','r',encoding="UTF-8")
    fajl.readline()
    sorokLista=fajl.readline()
    fajl.close()
    
    for i in range(0,len(sorokLista),1):
        lotto=sorokLista[i].strip()
        lottok=lotto.split("@")
        print(lottok)
        szamok=Hatoslotto(lottok[0],lottok[1],lotto[2],lotto[3])
        print(szamok)
        lotto_lista.append(szamok)
    fajl.close()
    return lotto_lista
    
def kiiras(lista):
    print(f"III/A, B:\n\tA húzások száma: {len(lista)}")