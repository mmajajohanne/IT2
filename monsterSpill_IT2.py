# coding=utf-8
from doctest import master
from pyexpat import native_encoding
import random

navn = ""

class Spiller:
    def __init__(self, navn, hp, angrepsstyrke):
        self.navn = navn
        self.hp = hp
        self.angrepsstyrke = angrepsstyrke
    
    def hit(self, styrke):
        self.hp -= styrke

class Monster:
    def __init__(self, hp, angrepsstyrke):
        self.hp = hp
        self.angrepsstyrke = angrepsstyrke

    def angrep(self, styrke):
        self.hp -= styrke

navn = input("Hva heter du? ")

spiller = Spiller(navn, 500, 50)
monster = Monster(70, 500)

print("Nå heter du", spiller.navn, ":)")

print("Velg en path i livet ditt:")
print("Gå bort til det vakre frukttreet skriv:0")
print("Gå bort til den mørke dype hulen skriv:1")
print("Gå bort til en gammel og forfallen kiste skriv:2")
valg1 = input("Ta valget ditt: ")

if valg1 == "0":
    print("Frukttreet bungner av ferske, røde og modne epler")
    valg2 = input("Vil du spise et eple? (ja)/(nei)")
    if valg2.lower() == "ja":
        spiller.hp += 10
        print("Du spiser eple og føler deg drit digg. Nå har du", spiller.hp, "hp")
    elif valg2 == "nei" or "Nei":
        print("Du går uten å spise et eple.")

    
    valg1 = "1"

if valg1 == "2":
    print("Kisten er vrien å åpne men du får omsider det til")
    print("Inni ligger det et sverd og en øks")
    valgVaapen = input("Hvilket våpen plukker du opp? Skriv '1' for øks og skriv '2' for sverd")
    if valgVaapen == "1":
        spiller.angrepsstyrke += 20
    else:
        spiller.angrepsstyrke += 21
    valg1 = "1"

if valg1 == "1":
    print("Nå bestemmer du deg for å gå inn i hulen.")
    valg3 = input("Vil du se stats før hulen? (ja)/(nei)")
    if valg3.lower() == "ja":
        print("Dette er hp:" , spiller.hp , "Dette er angrepsstyrken:"  , spiller.angrepsstyrke)
    else:
        pass

print("Inni hulen befinner det seg en ildrød skorpion med hp:", monster.hp)
print("Den vender seg og kryper fort mot deg.")

randomTall = random.randint(1,6)

if randomTall >= 4:
    print("Du reagerer raskt og tråkker på den med angrepsstyrken din på: ", spiller.angrepsstyrke)
    monster.angrep(spiller.angrepsstyrke)
    print("Monsteret har nå hp:", monster.hp)
else:
    print("Du klarer ikke å reagere og skorpionen angriper deg med angrepsstyrke:", monster.angrepsstyrke)
    spiller.hit(monster.angrepsstyrke)

if spiller.hp == 0:
    print("Du døde!")
elif spiller.hp != 0 and monster.hp != 0:
    print("Du angriper skorpionen tilbake med angrepsstyrke:" , spiller.angrepsstyrke)
    monster.angrep(spiller.angrepsstyrke)
    if monster.hp != 0:
        print("Du angriper skorpionen før den rekker å reagere igjen med angrepsstyrken", spiller.angrepsstyrke)
        monster.angrep(spiller.angrepsstyrke)

if monster.hp == 0:
    print("Du drepte monsteret!")

#Hei:)