"""
Este programa pide:
1. El precio de un producto (como cadena) y lo convierte a entero.
2. El impuesto (como cadena) y lo convierte a entero.
3. El descuento (como cadena) y lo convierte a flotante.
Luego imprime los tipos de datos antes y después de la conversión.
Imprimimos el total a pagar después de aplicar el impuesto y el descuento.
"""

precio = input("Ingrese el precio del producto: ")
print(type(precio))
precio = int(precio)
print(type(precio))

impuesto = input("Ingrese el impuesto (en porcentaje): ")
print(type(impuesto))
impuesto = int(impuesto)
print(type(impuesto))

descuento = input(" Ingrese el descuento (en porcentaje): ")
print(type(descuento))
descuento = float(descuento)
print(type(descuento))

total = precio + (precio * impuesto / 100) - (precio * descuento / 100)
print("Total a pagar: ",total)