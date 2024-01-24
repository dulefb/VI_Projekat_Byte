from tabla import Tabla
from igra import *

tabla1=Tabla()

    
tabla1.unesiBrojPolja(unosDimenzija())
tabla1.prikaziTablu()
igrac='O'
while True:
    if tabla1.odigrajPotez(unosPoteza(tabla1),igrac):
        if igrac=='X':
            igrac='O'
        else:
            igrac='X'
        tabla1.prikaziTablu()
    else:
        print("Nevalidan potez")
