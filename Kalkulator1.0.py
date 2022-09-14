#minikalkulator i python med en input
"""
tekst = str(input("Skriv inn regnestykke:"))
lastChar = tekst[len(tekst)-1]

operatorer =["+","-","*","/"]

def mult(a, b):
  return a * b
def div(a, b):
  return a / b
def pluss(a, b):
  return a + b
def minus(a, b):
  return a - b
def potens(a,b):
    return a**b

c = 0
for i in tekst:
    if i in operatorer:
        c = i
        a,b = tekst.split(c)
        a,b = float(a),float(b)


if c == "+":
    print(pluss(a, b))
elif c == "-":
    print(minus(a, b))
elif c == "*":
    print(mult(a, b))
elif c == "/":
    print(div(a, b))
elif c == "**":
    print(potens(a,b))

"""
operatorer =["+","-","*","/"]

tekst = str(input("Skriv inn regnestykke:"))
lastChar = tekst[len(tekst)-1]

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


