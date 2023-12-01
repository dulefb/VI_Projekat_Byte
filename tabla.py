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
        this.vrste={ chr(x):[['.' for j in range(0,9)] for i in range(0,this.n)] for x in range(this.pomeraj,this.pomeraj+this.n)}
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
                for j in range(0,9):
                    if (x%2==1 and i%2==0) or (x%2==0 and i%2==1):
                        prikazKolone+=f"{this.vrste[chr(x)][i][j]}"
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
           potez[1] in range(0,this.n) and
           int(potez[2])>0 and int(potez[2])<8
           and potez[3] in ['GD','GL','DD','DL']):
            return True
        else:
            return False