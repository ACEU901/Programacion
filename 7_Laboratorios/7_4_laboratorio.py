#Ejercicos enviado en clase

#Laboratorio 1

print(" Andrea viajo a Canada para aprender ingles. \n" 
        " Le parecio una experiencia muy divertida ")


#Laboratorio 2
nombre = input("Ingrese su nombre: ")
lugar = input("Ingresa el lugar a donde viajaste: ")
tema = input("Ingresa el tema que aprendiste en tu viaje: ")
adjetivo = input("Ingresa en una palabra (adjetivo) como te parecio esta experciencia: ")
habilidad = input("Ingresa que habilidad tenia el experto que conociste en el viaje: ")

print(nombre, " viajo a ", lugar, " para aprender sobre", tema,"\n"
      "Le parecio una experiencia muy", adjetivo, "\n"
       "Cuando llego, conocio a un experto en", habilidad)

#Laboratio 3
#Actividad 1
a = int(12)
b = float(25.36)
c = "Hola mundo"
print("El valor de a es: " ,a, " y es de tipo ", type(a))
print("El valor de c es: " ,b, " y es de tipo ", type(b))
print("El valor de c es: " ,c, " y es de tipo ", type(c))

#Actividad 2
a = "Hola "
b = "Python"
print(a+b)

#Actividad 3
mi_lista = ["Cejas", "Pestanas", "Ojos", "Frente", "Nariz"]
print(mi_lista[0])
print(mi_lista[4])

#Agregamos el valor "Boca" en nuestra lista
mi_lista.append("Boca")
print("--- Agregamos Boca a la lista --- ")
print(mi_lista)

#Eliminamos el lugar N°1 en la lista
mi_lista.pop(1)
print("--- Eliminamos el lugar N°1 a la lista --- ")
print(mi_lista)

#Actividad 4
mi_diccionario = {
    "nombre" : "Andrea",
    "edad" : "24",
    "ciudad" : "Santiago"
}
print("--- Mostramos el diccionario completo --- ")
print(mi_diccionario)

mi_diccionario ["ocupacion"]=  "Sin trabajo"
print("--- Agregamos la clave 'Ocupacion' --- ")
print(mi_diccionario)

#Actividad 5
a = True
b = False

suma = a + b
print(suma)

c = 25
suma_con_entero = b + c
print(suma_con_entero)

d = "Hola Mundo"
suma_con_cadena = a + d
print(suma_con_cadena)

