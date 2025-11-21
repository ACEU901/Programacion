"""
1. Ejercicios para el tipo de dato int (entero)
 
Empresa: "LogiExpress" — Empresa de envíos nacionales
Situación:
El departamento de operaciones necesita calcular la cantidad total de paquetes procesados en una jornada.
Ejercicio:
Pide al usuario ingresar:
Cantidad de paquetes enviados en la mañana
 
Cantidad de paquetes enviados en la tarde
 
Cantidad de paquetes enviados en la noche
 
Objetivo:
Suma los valores y muestra el total de paquetes procesados.
"""

paq_mañana = input("Ingrese la cantidad de paquetes enviados en la mañana: ")
paq_mañana = int(paq_mañana)

paq_tarde = input("Ingrese la cantidad de paquetes enviados en la tarde: ")
paq_tarde = int(paq_tarde)

paq_noche = input("Ingrese la cantidad de paquetes enviados en la noche: ")
paq_noche = int(paq_noche)

total_paq = paq_mañana + paq_tarde + paq_noche
print("El total de los paquetes procesados es: ",total_paq)