calculadora = True

while(calculadora):
    n = input("1.Sumar // 2.Restar // 3.Multiplicar // 4.Dividir // 5.Salir \n")
    n = int(n)
    match(n):
        case 1:
            a = int(input("Escriba un numero: "))
            b = int(input("Escriba un numero: "))
            print(a + b)
        case 2:
            a = int(input("Escriba un numero: "))
            b = int(input("Escriba un numero: "))
            print(a - b)
        case 3:
            a = int(input("Escriba un numero: "))
            b = int(input("Escriba un numero: "))
            print(a * b)
        case 4:
            a = int(input("Escriba un numero: "))
            b = int(input("Escriba un numero: "))
            print(a / b)
        case 5:
            calculadora = False
        case _:
            print("No se encuentra")
