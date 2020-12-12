import datetime
from modulo import sumar
from random import randrange, choice

def seeDate():
    print(datetime.date.today())

def numAleatorioHastaOtroNumero():
    print(randrange(10))

def generateNumberAyB():
    print(random.randint(10, 20))

def test():
    x = 90
    if (x > 50) :
        sumar(45,5)
    else :
        sumar(45,5)
