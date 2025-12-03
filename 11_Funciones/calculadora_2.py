def suma(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    return numero1 + numero2

def resta(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    return numero1 * numero2

def division(numero1, numero2):
    numero1 = int(numero1)
    numero2 = int(numero2)
    return numero1 / numero2

calculadora = "Si"
while(calculadora == "Si"):
    calculadora = "Si"
    menu = int(input("Seleccione la operacion a realzar: 1.Suma 2.Resta 3.Multiplicacion 4.Division 5.salir: "))
    match menu:
        case 1:
            numero1 = input("ingrese el primer numero: ")
            numero2 = input("ingrese el segundo numero: ")
            print("la suma es: ", suma(numero1, numero2))
        case 2:
            numero1 = input("ingrese el primer numero: ")
            numero2 = input("ingrese el segundo numero: ")
            print("la resta es: ", resta(numero1, numero2))
        case 3:
            numero1 = input("ingrese el primer numero: ")
            numero2 = input("ingrese el segundo numero: ")
            print("la multiplicacion es: ", multiplicacion(numero1, numero2))
        case 4:
            numero1 = input("ingrese el primer numero: ")
            numero2 = input("ingrese el segundo numero: ")
            print("la division es: ", division(numero1, numero2))
        case 5:
            calculadora = "No"
        case _:
            print("Opcion no valida")