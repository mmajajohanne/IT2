"""
Varer som skal brukes: 
epler (Pink) koster 20 kr pr kg, 
appelsiner (Jaffa) koster 25 kr pr kg
ananas (hel) koster kr 15 pr stk
"""


class Vare: 
    def __init__(self, navn,kategori, pris):
        self.navn = navn
        self.kategori = kategori
        self.pris = pris

    def getpris(self):
        return self.pris

    def getnavn(self):
        return self.navn

liste_vare = []
liste_pris = []
def main():
    Vare1 = Vare("Epler", "Pink",20)
    Vare2 = Vare("Appelsiner","Jaffa", 25)
    Vare3 = Vare("Ananas","hel",15)

    Shopping = True
    while Shopping == True:
        svar = int(input("Skriv inn 1 for eple, 2 for appelsin og 3 for ananas:"))
        antall = int(input("Hvor mye av varen vil du ha? (skriv heltall uten enhet)"))
        if svar == 1:
            for i in range(0,(antall)):
                pris = Vare1.getpris()
                liste_pris.append(pris)
                navn = Vare1.getnavn()
                liste_vare.append(navn)
        if svar == 2:
            for i in range(0,(antall)):
                liste_pris.append(Vare2.getpris())
                liste_vare.append(Vare2.getnavn())
        if svar == 3:
            for i in range(0,(antall)):
                liste_pris.append(Vare3.getpris())
                liste_vare.append(Vare3.getnavn())

        print("")
        svar2 = int(input("Trykk 1 hvis du vil fortsette, trykk 2 hvis du vil slutte å handle:"))
        if svar2 == 2:
            Shopping = False
    print("")
    print("her er varefordelingen din:")
    epler = liste_vare.count("Epler")
    appelsiner = liste_vare.count("Appelsiner")
    ananas = liste_vare.count("Ananas")
    print("Du kjøper:", epler,"kg epler. Det vil koste deg", (epler*Vare1.pris),"kr.")
    print("Du kjøper:", appelsiner,"kg appelsiner. Det vil koste deg", (appelsiner*Vare2.pris),"kr.")
    print("Du kjøper:", ananas,"ananaser. Det vil koste deg", (ananas*Vare3.pris),"kr.")
    print("Totalsummen din er:", sum(liste_pris))
main()

