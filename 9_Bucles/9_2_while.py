#importamos los numeros random
from random import *
#creamos la variable con la condicion que tenga un numero random y este dentro de 0 y 100
numero = randint(0,100)

numeroMio = 0

while numero != numeroMio:
    numeroMio = input("Ingrese el numero: ")
    numeroMio = int(numeroMio)
    if numero == numeroMio:
        print("Ganaste")
    elif numero > numeroMio:
        print("Tu numero es menor")
    else:
        print("tu numero es mayor")


