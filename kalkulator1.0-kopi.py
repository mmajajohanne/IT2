#minikalkulator i python med en input

operatorer =["+","-","*","/"]

k= 0
inp = str(input("Skriv inn regnestykke:"))
tekst = []
telle = 0

#jobber foreløpig med denne delen av programmet, har ikke helt fått til å
#legge til hvert tall og operator i en samlet liste.
for i in inp:
    telle = telle + 1
    if i=="+" or i =="-" or i == "/"  or i =="*":
        while k<telle:
            tekst.append(inp[k])
            k = k+1
        tekst.append(inp.index(i))
        


#resten av programmet funker (hvis man har lista)

deling = operatorer.index("/")
while (deling != -1):
    tekst.insert(deling, 2, tekst[deling] / tekst[deling+ 1])
    operatorer.insert(deling, 1)
    deling = operatorer.index("/")

gange = operatorer.index("*")
while (gange != -1):
    tekst.insert(gange, 2, tekst[gange] / tekst[gange+ 1])
    operatorer.insert(gange, 1)
    gange = operatorer.index("*")

add = operatorer.index("+")
while (add != -1):
    tekst.insert(add, 2, tekst[add] / tekst[add+ 1])
    operatorer.insert(add, 1)
    add = operatorer.index("+")

minus = operatorer.index("-")
while (minus != -1):
    tekst.insert(minus, 2, tekst[minus] / tekst[minus+ 1])
    operatorer.insert(minus, 1)
    minus = operatorer.index("-")

print(tekst[0])



