#coding=utf-8

from bibliotek import SumListeFunk as summe
l = [1,2,3,4]
print(summe(l))

from bibliotek import SnittListeFunk as snitt
l2 = [1,2,3,4,4,5,6]
print(snitt(l2))

from bibliotek import StorstIListe as strst
l3 = [28,34.3,78,2]
print(strst(l3))


def palindromTest(navn, ord):
     #funksjon som returnerer TRUE hvis ordet er et palindrom og False hvis det ikke er det
     print ("Hei", navn,"! Er ordet du har valgt et palindrom?")
     return ord == ord[::-1]
print(palindromTest(maja,civic))