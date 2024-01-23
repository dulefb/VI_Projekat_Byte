from tabla import Tabla
def unosDimenzija():
    print("Unesi dimenziju tabele")
    nInput=None
    broj=0
    while True:
        nInput=input()
        if(nInput.isdigit()):
            if(int(nInput)<8 or int(nInput)>16 or int(nInput)%2==1):
                print("Unesite paran broj u razmaku od 8 do 16\n")
            else:
                broj=int(nInput)
                break
        else:
            print("Morate da unesete validan paran broj u razmaku od 8 do 16\n")
    
    return broj

def unosPoteza(tabla:Tabla):
    print("Unesi potez:<Vrsta> <Kolona> <Broj_figura> <Smer>")
    nInput=None
    broj=0
    while True:
        nInput=input()
        newN = nInput.split(" ")
        if(len(newN)!=4):
            print("Unesite validan potez")
        else:
            if tabla.potezIsValid(newN):
                return newN
            else:
                print("Unesite validan potez")
        tabla.prikaziTablu()