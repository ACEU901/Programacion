print("--- EVALUADOR DE RENDIMIENTO ---")

nom_empleado = input("Ingrese el nombre del empleado: ")
calificacion = input("Ingrese calificación (A, B, C, D): ")
cargo = input("¿Es Líder? (escriba SI o NO): ")

# Convertimos la respuesta del cargo a un booleano 
es_lider = "LIDER" if cargo == "SI" else "EMPLEADO"

datos_evaluacion = (calificacion, es_lider)

match datos_evaluacion:
    case (_, "LIDER"):
        print(f"{nom_empleado}: Eres un lider (Liderazgo)")
    case ("A", _):
        print(f"{nom_empleado}: Calificación Excelente")

    case ("B", _):
        print(f"{nom_empleado}: Calificación Buena")

    case ("C", _):
        # Aquí no importa si es líder o no, el mensaje es regular
        print(f"{nom_empleado}: Calificación Regular")

    case ("D", _):
        print(f"{nom_empleado}: Calificación Deficiente")

    case _:
        print("---- Dato inválido ----")