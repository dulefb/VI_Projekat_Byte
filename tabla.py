class Tabla:
    def __init__(this):
        this.n=0
        this.pomeraj=0
        this.vrste=None
        this.stekX=0
        this.stekO=0
        this.pocetnaVrednost=0
    
    def unesiBrojPolja(this,n:int):
        this.n=n
        this.pomeraj=65
        this.vrste={ chr(x):[['.' for j in range(0,8)] for i in range(0,this.n)] for x in range(this.pomeraj,this.pomeraj+this.n)}
        if(n>10):
            this.pocetnaVrednost=1
        for x in range(this.pomeraj+this.pocetnaVrednost,this.pomeraj+this.n-this.pocetnaVrednost):
            for i in range(0 if x%2==1 else 1,this.n,2):
                if x-this.pomeraj<this.n-this.pocetnaVrednost-1 and x-this.pomeraj>0+this.pocetnaVrednost:
                    this.vrste[chr(x)][i].pop()
                    if x%2==0:
                       this.vrste[chr(x)][i].append('X')
                    else:
                        this.vrste[chr(x)][i].append('O')

    def prikaziTablu(this):
        prikazVrste=' '*6
        for x in range(this.pomeraj,this.pomeraj+this.n):
            prikazVrste+=str(x-this.pomeraj+1)+' '*8
        print(prikazVrste)
        prikazVrste=''
        for x in range(this.pomeraj,this.pomeraj+this.n):
            prikazVrste+=chr(x)+' '
            prikazKolone=''
            for i in range(0,this.n):
                for j in range(0,8):
                    if (x%2==1 and i%2==0) or (x%2==0 and i%2==1):
                        prikazKolone+=f"{this.vrste[chr(x)][i][j-1]}"
                    else:
                        prikazKolone+=f"{' '}"
            prikazVrste+=prikazKolone
            prikazVrste+='\n'
        print(prikazVrste)
    
    def krajIgre(this):
        ukupnoFigura=0
        if this.n>10:
            ukupnoFigura=2*(this.n/2)*((this/2)-1)
        else:
            ukupnoFigura=2*(this.n/2)*((this/2)-2)
        brojMogucihStekova=ukupnoFigura/8
        if(this.stekX/brojMogucihStekova>0.5 or this.stekO/brojMogucihStekova>0.5):
            return True
        else:
            return False
        
    def potezIsValid(this,potez):
        if(potez[0] in [chr(x) for x in range(this.pomeraj,this.pomeraj+this.n)] and 
           int(potez[1]) in range(0,this.n) and
           int(potez[2])>=0 and int(potez[2])<8
           and potez[3] in ['GD','GL','DD','DL']):
            return True
        else:
            return False
        
    def checkStackOnPlace(this,vrsta,kolona,broj_figura):
        count=len(list(filter(lambda x:x=='X' or x=='O',this.vrste[vrsta][kolona])))
        if count==8 or count+broj_figura>=8:
            return False
        else:
            return True
        
    def checkClosePlacesAndReturnValidPotez(this,potez):
        for i in range(0,6):
            validniPotezi={}
            foundValidPotez=False
            #GORE LEVO
            if this.checkStackOnPlace(chr(ord(potez[0])-1),int(potez[1])-2,int(potez[2])):
                validniPotezi['GL']=[chr(ord(potez[0])-1),int(potez[1])-2]
                foundValidPotez=True
            #GORE DESNO
            if this.checkStackOnPlace(chr(ord(potez[0])-1),int(potez[1]),int(potez[2])):
                validniPotezi['GD']=[chr(ord(potez[0])-1),int(potez[1])]
                foundValidPotez=True
            
            #DOLE LEVO
            if this.checkStackOnPlace(chr(ord(potez[0])+1),int(potez[1])-2,int(potez[2])):
                validniPotezi['DL']=[chr(ord(potez[0])+1),int(potez[1])-2]
                foundValidPotez=True
            
            #DOLE DESNO
            if this.checkStackOnPlace(chr(ord(potez[0])+1),int(potez[1]),int(potez[2])):
                validniPotezi['DD']=[chr(ord(potez[0])+1),int(potez[1])]
                foundValidPotez=True

            if foundValidPotez:
                break
        return validniPotezi
    
    def odigrajPotez(this,potez,igrac):
        #IGRAC JE ZADAT SA X ili O
        #POTEZ JE OBLIKA [<vrsta> <kolona> <broj_figura> <smer>]
        novaTabla=this.vrste.copy()
        if not this.potezIsValid(potez):
            return False
        
        index=0
        currentField = this.vrste[potez[0]][int(potez[1])].copy()
        currentField.reverse()
        for x in currentField:
            if x=='X' or x=='O':
                index+=1
        #if currentField[index]!=igrac:
            #return False
        
        validniPotezi = this.checkClosePlacesAndReturnValidPotez(potez)
        if len(validniPotezi)>0:
            vrsta=validniPotezi[potez[3]][0]
            kolona=validniPotezi[potez[3]][1]
            #FIGURE KOJE SE POMERAJU
            elementsToMove=[]
            for i in range(0,int(potez[2])):
                elementsToMove.append(this.vrste[potez[0]][int(potez[1])].pop())
                this.vrste[potez[0]][int(potez[1])].reverse()
                this.vrste[potez[0]][int(potez[1])].append('.')
                this.vrste[potez[0]][int(potez[1])].reverse()
            
            #FIGURE KOJE TREBA VRATITI
            elements=[]
            pom=novaTabla[vrsta][kolona].pop()
            while pom!='.':
                elements.append(pom)
                pom=novaTabla[vrsta][kolona].pop()

            for el in elementsToMove:
                novaTabla[vrsta][kolona].append(el)
            for el in elements:
                novaTabla[vrsta][kolona].append(el)

            this.vrste=novaTabla
            return True
        else: 
            return False