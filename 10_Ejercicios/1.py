i = int(input("Ingrese el codigo numerico: "))

if i % 2 == 0 and i % 3 == 0:
        print("Producto VIP")
elif i % 2 == 0:
        print("Producto estandar")
elif i % 3 == 0:
        print("Producto premium")
else:
        print("Sin categoria")