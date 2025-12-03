nombres = ["Carlos", "Andrea", "Pablo", "Anastasia", "Carolina"]

for nombre in nombres:
    if nombre == "Carlos":
        print("Hola Carlos de contabilidad, ten un lindo dia")
    elif nombre.startswith("A"):
        print("Tu nombre inicia con A:", nombre)
    else:
        print("Hola", nombre)