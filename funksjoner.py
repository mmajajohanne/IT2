
#coding=utf-8

#utforskning rekursive funksjoner i python
#fakultet (!) av valgt tall
def rekFunk1(n):
   if n == 1:
       return n
   else:
       return rekFunk1(n-1)*n

tall = input(int("Skriv inn heltallet du vil finne fakultet av: "))

#må teste om tallet er negativt
if tall < 0:
   print("Du kan ikke ta fakultet for et negativt tall!")
elif tall == 0:
   print("Fakultet av 0 er 1")
else:
   print("Fakultet av", tall, "er", rekFunk1(tall))

#--------------------------------------------------------

#kan også bruke rekursive funksjoner for å finne ut om et ord er et palindrom (?)
#uten rekursiv funksjon:
def palindromTest(word):
     #return TRUE hvis ordet er et palindrom og False hvis det ikke er det
     return word == word[::-1]

print(palindromTest("sko"))
print(palindromTest("civic"))

def palindromTest(navn, ord):
     #funksjon som returnerer TRUE hvis ordet er et palindrom og False hvis det ikke er det
     print ("Hei", navn,"! Er ordet du har valgt et palindrom?")
     return ord == ord[::-1]
print(palindromTest(maja,civic))
#--------------------------------------------------------

#med rekursiv funksjon: (kanskje ikke så nødvendig.. men men)
def rekFunk2(word):
     if len(word) <= 1:
         return True
     else:
         return word[0] == word[-1] and rekFunk2(word[1:-1])

#test (uten rekursiv)
print(rekFunk2("")) #true
print(rekFunk2("a")) #true

#test m rekursiv
print(rekFunk2("sko")) #false
print(rekFunk2("racecar")) #true
print(rekFunk2("troglodyte")) #false
print(rekFunk2("civic")) #true

