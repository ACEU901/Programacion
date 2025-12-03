cod_rapido = True

while(cod_rapido):
    n = input(" 1.Crear ticket\n 2.Escalar a supervisor\n 3.Cerrar ticket\n")
    n = int(n)
    match(n):
        case 1:
            print("Creaste un ticket")
        case 2:
            print("Su solicitud ha sido escalada a su supervisor")
        case 3:
            print("Su ticket ha sido cerrado con exito")
        case _:
            print("---- CODIGO INVALIDO, INTENTELO NUEVAMENTE ---- ")