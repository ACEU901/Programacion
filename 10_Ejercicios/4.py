sensor = True

while(sensor):
    print("Ingrese el codigo del sensor textualmente(respetando mayusculas y minusculas) ")
    n = input("ERR" "\n" "LOW" "\n" "OK" "\n")
    match(n):
        case "ERR":
            print("---- Error Critico ----")
        case "LOW":
            print("---- Bateria baja ----")
        case "OK":
            print("---- Funcionando normal ----")
        case _:
            print("---- Estado desconocido ---- ")