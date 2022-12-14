# "monster vs helt"-spill vurdering 1 IT2
# -*- coding: utf-8 -*
import random 
import time
import math
import sys

#lånt av areeba:-)
class bcolors: 
    PURPLE = '\033[95m' #Purple text 
    BLUE = '\033[94m' #Blue text - Gameinfo
    CYAN = '\033[96m' #Cyan text
    GREEN = '\033[92m' #Green text 
    WARNING = '\033[93m' #Yellow text 
    FAIL = '\033[91m' #Red text - Attack-message or dead-message
    ENDC = '\033[0m' #End text color 
    BOLD = '\033[1m' #Bold text 
    UNDERLINE = '\033[4m' #Puts in Underline


class helt:
    """
    Klasse for Helten.
    
    Attributter
    --------------
    Hhelse : int
        heltens samlede helse
    Hsverdangrep : int
        angrepspoeng med sverd
    Hhell : int
        sannsynligheten for at helten treffer monsteret i et angrep
    Hbueangrep : int
        angrepspoeng med bue
    Hforsvar : int
        hvor mange av motstanderens angrepspoeng som blokkeres 
    Hmagi : int
        angrepspoeng med magi
    Hnavn : str
        heltens navn
    ----------------
    """
    
    def __init__(self, Hhelse, Hsverdangrep, Hhell, Hbueangrep, Hforsvar, Hmagi, Hnavn):
        self.helse = Hhelse
        self.sverdangrep = Hsverdangrep
        self.hell = Hhell
        self.bueangrep = Hbueangrep
        self.forsvar = Hforsvar
        self.magi = Hmagi
        self.navn = Hnavn

    def gethelse(self):
        """Metode for å returnere heltens helse."""
        return self.helse
    def getsverdangrep(self):
        """Metode for å returnere heltens sverdangrepspoeng."""
        return self.sverdangrep
    def gethell(self):
        """Metode for å returnere heltens hell."""
        return self.hell
    def getbueangrep(self):
        """Metode for å returnere heltens bueangrepspoeng."""
        return self.bueangrep
    def getforsvar(self):
        """Metode for å returnere heltens forsvarspoeng."""
        return self.forsvar
    def getmagi(self):
        """Metode for å returnere heltens magiangrepspoeng."""
        return self.magi
    def getnavn(self):
        """Metode for å returnere heltens navn."""
        return self.navn


    def sethelse(self, newhelse):
        """Metode for å endre helsen."""
        self.helse = newhelse
    def setsverdangrep(self, newsverdangrep):
        """Metode for å endre sverdangrepspoengene."""
        self.sverdangrep = newsverdangrep
    def sethell(self, newhell):
        """Metode for å endre hellen."""
        self.hell = newhell
    def setbueangrep(self, newbueangrep):
        """Metode for å endre bueangrepspoengene."""
        self.bueangrep = newbueangrep
    def setforsvar(self, newforsvar):
        """Metode for å endre forsvarspoengene."""
        self.forsvar = newforsvar
    def setmagi(self, newmagi):
        """Metode for å endre magiangrepspoengene."""
        self.magi = newmagi


class monster:
    """
    Klasse for Monsteret.
    
    Attributter
    --------------
    Mhelse : int
        monsterets samlede helse
    Mangrep : int
        monsterets angrepspoeng
    Msjanse : int
        sansynnlighetstall
    Mnavn : str
        monsterets navn
    ----------------
    """
    
    def __init__(self, Mhelse, Mangrep, Msjanse, Mnavn):
        self.helse = Mhelse
        self.sverdangrep = Mangrep
        self.sjanse = Msjanse
        self.navn = Mnavn

    def gethelse(self):
        """Metode for å returnere monsterets helse."""
        return self.helse
    def getsverdangrep(self):
        """Metode for å returnere monsterets angrepspoeng."""
        return self.sverdangrep
    def getsjanse(self):
        """Metode for å returnere monsterets sjanse."""
        return self.sjanse
    def getnavn(self):
        """Metode for å returnere monsterets navn."""
        return self.navn

    def sethelse(self, newhelse):
        """Metode for å endre helsen."""
        self.helse = newhelse
    def setsverdangrep(self, newsverdangrep):
        """Metode for å endre angrepspoengene."""
        self.sverdangrep = newsverdangrep
    def setsjanse(self, newsjanse):
        """Metode for å endre sjanse."""
        self.sjanse = newsjanse



class boss (monster):
    """
    Klasse for monsterversjonen: boss.
    
    Arvede attributter
    --------------
    Mhelse : int
        boss monsterets samlede helse
    Mangrep : int
        boss monsterets angrepspoeng
    Msjanse : int
        (!!!!!!!!!!!!!!!!!)
    Mnavn : str
        boss monsterets navn
    ----------------
    Nye attributter
    ---------------
    Mspesialangrep : int
        boss monsterets spesialangrepspoeng
    
    """
    
    def __init__(self, Mhelse, Mangrep, Msjanse, Mnavn, Mspesialangrep):
        super().__init__(Mhelse, Mangrep, Msjanse, Mnavn)

        self.spesialangrep = Mspesialangrep

    def getSuper(self):
        """Metode for å returnere spesialangrepsstyrken."""
        return self.spesialangrep
    
    def setSuper(self, newspesialangrep):
        """Metode for å endre spesialangrepsstyrken."""
        self.spesialangrep = newspesialangrep



def createClass():
    """
    Finner verdier til atributtene i Helt.
        
        Parametere:
        ------------
            none
            
        Returnerer:
        ------------
            heltsverdangrep, helthell, heltforsvar, heltmagi, heltnavn
            
    """
    a = input("Velkommen.... Er du mer defensiv [1] eller offensiv [2] i kamp?")
    while a != "1" and a != "2":
        print(f"{bcolors.FAIL}(ikke et gyldig valg)...{bcolors.ENDC}")
        a = input(f"Er du mer defensiv [1] eller offensiv [2] i kamp?")

    if a == "1":
        heltsverdangrep = 5
        heltforsvar = 10

    elif a == "2":
        heltsverdangrep = 10
        heltforsvar = 5

    b = input ("Trykk enter for å trekke et tall..")    #b brukes aldri videre (kun for at bruker skal kunne interagere)
    time.sleep(0.2)
    print("...")
    helthell = random.randint(0,10)
    print ("Du trakk", helthell)
    print ("Helten din har hell på", helthell, " av 10")

    c = input ("Vil du være en bueskytter [1] eller magiker [2] ?" )
    while c != "1" and c != "2":
        print(f"{bcolors.FAIL}(ikke et gyldig valg)...{bcolors.ENDC}")
        c = input ("Vil du være en bueskytter [1] eller magiker [2] ?")

    
    if a == "1":
        heltbueangrep = 10
        heltmagi = 5

    elif a == "2":
        heltbueangrep = 5
        heltmagi = 10

    heltnavn = input("Hva er navnet til helten din?")
    print("...")
    print("Velkommen", heltnavn, "!")
    print("Du befinner deg alene i en stor gladiatorarena. Du er omringet av høye jernvegger \nog foran deg er det en lukket jernport.\n")
    print("Her er egenskapene dine:")


    return(heltsverdangrep, helthell, heltbueangrep, heltforsvar, heltmagi, heltnavn)
                


def monsterGen(levelBoss):
    """
    Finner verdier til atributtene i Monster eller Monster: Boss.
    
        Parametere:
        ---------------
            levelBoss : boolean
                bestemmes av den tilfeldig valgte verdien til variabelen bosssjanse
                
        Returnerer:
        ------------------
            Hvis spiller er på 'vanlig monster' nivå:
                helse, sverdangrep, sjanse, adjektiv+" "+skapning (navn)
            Hvis spiller er på 'boss monster' nivå:
                helse, sverdangrep, sjanse, adjektiv+" "+skapning (navn), spesialangrep
                
    """
    #bruker eksterne tekstfiler (python moduler) for å generere et tilfeldig navn til monsteret
    file = open("txtFiler/adjektiv.txt","r")
    lines = file.readlines()
    adjektiv = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    file = open("txtFiler/skapning.txt","r")
    lines = file.readlines()
    skapning = lines[random.randint(0,len(lines)-1)][:-1]
    file.close
    

    if levelBoss == False:      #gir 'vanlig monster' verdier til attributtene
        helse = random.randint(50,100)
        sverdangrep = random.randint(10,15)
        sjanse = random.randint(1,10)

        return monster(helse, sverdangrep, sjanse, adjektiv+" "+skapning)

    else:                       #gir 'boss monster' verdier til attributtene
        helse = random.randint(200,250)
        sverdangrep = random.randint(20,40)
        sjanse = random.randint(1,8)
        spesialangrep = random.randint(100,200)

        return boss(helse, sverdangrep, sjanse, adjektiv+" "+skapning, spesialangrep)



def monstersverdangrep(hitsjanse, sverdangrepValue, navn, forsvar):
    """
    Når monsteret angriper helten.
    
        Parametere:
        ---------------
            hitsjanse : int
                sjanse til monsteret
            sverdangrepValue : int
                angrepspoengene til monsteret
            navn : str
                navnet til monsteret
            forsvar : int
                forsvarspoengene til helten
                
                
        Returnerer:
        ------------------
            tap : int
                antall helsepoeng helten mister
                
    """
    print(navn, "stormer mot deg i et angrep...")
    hit = random.randint(0,10)
    if hitsjanse >= hit:
        print("den treffer helten!!!")
        tap = sverdangrepValue - forsvar
        print("Du mister", tap, "av helsen din")
        return math.ceil(tap)
    else:
        print("Monsteret bommer og treffer deg ikke!")
        return 0



def hitsjanse(hell):
    """
    Finner ut hvorvidt helten treffer monsteret eller ikke når hen angriper.
    
        Parametere:
        ---------------
            hell : int
                sannsynligheten for å treffe
                
        Returnerer:
        ------------------
            True/False : boolean
                
    """
    hit = random.randint(0,4) #hvis man har hell over 4 vil man alltid treffe
    if hell < hit:
        print("Du bomma på monsteret!")
        return False
    else:
        print("Du traff monsteret!")
        return True



def isDead(helse):
    """
    Tester om helten er død.
    
        Parametere:
        ---------------
            helse : int
                helsen til helten
                
        Returnerer:
        ------------------
            True/False : boolean
                True hvis helse <= 0
                False hvis helse > 0
                
    """
    if helse < 1:
        return True
    else:
        return False



def gave(hell, genspiller):
    """
    Avgjør hva helten får når monsteret dør.
    
        Parametere:
        ---------------
            hell : int
                sannsynligheten for å få gave (samme som sannsynligheten for å treffe)
                
        Returnerer:
        ------------------
            none
                
    """
    gavesjanse = random.randint(0,4)
    if hell < gavesjanse:
        print("Eiendelene til monsteret ble ødelagt i kampen") #hvis man har sjanse > 4 får man alltid gave

    else:
        #henter ut tilfeldig gave fra en av tekstfilene
        tableI = random.randint(0,4)
        gaveTableList = ["ting","bueangrep","forsvar","magi","sverdangrep"] #kan enkelt legge til flere typer gaver/ting med denne listen
        TingType = gaveTableList[tableI]
        file = open("txtFiler/"+TingType+".txt","r")
        lines = file.readlines()

        print("Blant monsterets eiendeler finner du en/et:")
        Ting = random.randint(0,len(lines)-1)

        TingLine = lines[Ting]
        splitTingLine = TingLine.split(",")

        navn = splitTingLine[0]
        value = int(splitTingLine[1])

        print(navn,"!")
        print("")
        
        #hvis man får et våpen, blir angrepspoengene i riktig kategori høyere
        if TingType == "sverdangrep":
            genspiller.setsverdangrep(genspiller.getsverdangrep()+value)
            print("Angrepspoengene dine med sverd er nå::")
            print(genspiller.getsverdangrep())

        elif TingType == "bueangrep":
            genspiller.setbueangrep(genspiller.getbueangrep()+value)
            print("Angrepspoengene dine med bue er nå::")
            print(genspiller.getbueangrep())

        elif TingType == "forsvar":
            genspiller.setforsvar(genspiller.getforsvar()+value)
            print("Forvarsevnen din har økt til:")
            print(genspiller.getforsvar())

        elif TingType == "magi":
            genspiller.setmagi(genspiller.getmagi()+value)
            print("Angrepspoengene dine med magi er nå:")
            print(genspiller.getmagi())

        else:
            
            if splitTingLine[2] == "hell":
                genspiller.sethell(genspiller.gethell()+value)
                print("Lykken din har økt til:")
                print(genspiller.gethell())

            elif splitTingLine[2] == "helse":
                genspiller.sethelse(genspiller.gethell()+value)
                print("Helsen din har økt til:")
                print(genspiller.gethelse())

                                     
def gameOver(monsterDead):
    """
    Tester om monsteret er død.
    
        Parametere:
        ---------------
            monsterDead : boolean
                True hvis monster har helse <= 0
                False hvis monster har helse > 0
                
        Returnerer:
        ------------------
            none
                
    """
    if monsterDead == True:
        print("---------------------")
        print("Du blir plutselig veldig svimmel, og det svartner for øynene dine...")
        print("....")
        print(".....")
        print("Du våkner opp i en ny gladiatorarena...En ny kamp venter deg!")

    else:
        print("---------------------")
        print("Du døde! Spillet er over :(")
        sys.exit() #tvinger programmet til å slutte å kjøre
        

def kamp(genmonster, genhelt):
    """
    Kjører kamp.
    
        Parametere:
        ---------------
            genmonster : object
                det genererte monsteret
            genhelt : object
                den genererte helten
                
        Returnerer:
        ------------------
            True/False : boolean
                True hvis helten overlever kampen
                False hvis helten dør
                
    """
    kamp = True

    print("\nPorten på andre siden av arenaen åpner seg sakte...")
    print("Ut kommer en", genmonster.getnavn(),"!")
    print("Den har disse egenskapene:")
    print(vars(genmonster))

    while kamp == True:
        print("Velg angrepsstype:")
        print("1. Sverd \n2. Bue \n3. Magi")
        valg = input()

        while valg != "1" and valg != "2" and valg != "3":
            print("(ugyldig valg)\n")
            print("1. Sverd \n2. Bue \n3. Magi")
            valg = input()

        if valg == "1":
            skade = genhelt.getsverdangrep()

        elif valg == "2":
            skade = genhelt.getbueangrep()

        else:
            skade = genhelt.getmagi()

        print("Du går til angrep...")
        hit = hitsjanse(genhelt.gethell())

        if hit == True:
            genmonster.sethelse(genmonster.gethelse() - skade)
            print("Monsteret har nå helse =", genmonster.gethelse(),"\n")

        #else:
            
        monsterDead = isDead(genmonster.gethelse())

        if monsterDead == False:
            genhelt.sethelse(genhelt.gethelse() - monstersverdangrep(genmonster.getsjanse(), genmonster.getsverdangrep(), genmonster.getnavn(), genhelt.getforsvar()))
            
            spillerDead = isDead(genhelt.gethelse())

            if spillerDead == True:
                kamp = False
                return False

            else:
                print("Helten har nå helse=", genhelt.gethelse())

        else:
            kamp = False
            print("Gratulerer, du har beseiret monsteret!\n")
            print("...la den kanskje igjen noen eiendeler?")
            print("...")
            gave(genhelt.gethell(), genhelt)

            return True


def levelGenerator(spiller, level):
    """
    Beregner level og hvorvidt neste monster er vanlig eller boss.
    
        Parametere:
        ---------------
            spiller : dict
                data fra helt-objektet
            level : int
                nivå (fra 1-4)
                
        Returnerer:
        ------------------
            none
                
    """
    maxAntallMonstre = math.ceil(level*5)
    for x in range(0, maxAntallMonstre):
        bosssjanse = random.randint(1,10)
        if bosssjanse > 7:
            levelBoss = True

        else:
            levelBoss = False

        spillerDead = kamp(monsterGen(levelBoss), spiller)
        gameOver(spillerDead)


def main():
    """
    Driver bak hele spillet.
    
        Parametere:
        ---------------
            none
                
        Returnerer:
        ------------------
            none
                
    """
    classData = createClass()
    spiller = helt(100, classData[0], classData[1], classData[2], classData[3], classData[4], classData[5])
    print(vars(spiller))
    print("Level 1...")
    levelGenerator(spiller, 1)
    print("Level 2...")
    levelGenerator(spiller, 2)
    print("Level 3...")
    levelGenerator(spiller, 3)
    print("Level 4...")
    levelGenerator(spiller, 4)
    print("\nWOW DU VANT GLADIATORKAMPEN!!!!!")
    print(vars(spiller))
    
    
main()
#