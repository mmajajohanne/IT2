#coding=utf-8
"""
Lag et bibliotek som inneholder funksjoner som utfører disse oppgavene (og test biblioteket):
- Summen av tallene i en liste
- Gjennomsnittet av tallene i en liste
- Det største tallet i en liste"""

def SumListeFunk(liste):
    """Funksjon som manuelt regner ut summen av alle leddene i en oppgitt liste"""
    s = 0
    for i in range(0,len(liste)):
        s = s + liste[i]
    return s

def SnittListeFunk(liste):
    """Funksjon som regner ut gjennomsnittet av tallene i en oppgitt liste"""
    s = 0
    for i in range(0,len(liste)):
        s = s + liste[i]
    snitt = s/len(liste)
    return snitt


def StorstIListe(liste):
    """Funksjon som finner det største tallet i en liste"""
    a = 0
    for i in range(0,len(liste)):
        if liste[i] > a:
            a = liste[i]
    return a



