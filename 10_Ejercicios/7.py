turno = 1 
    
print("--- INICIO DE JORNADA LOGÍSTICA ---")

while turno <= 8:
    print(f" Registrando turno operativo #{turno}")

    if turno == 4:
        print("------- CAMBIO DE EMPLEADO (RELEVO EN PROCESO....)-------")

    turno += 1 

print("--- Registro completo: Fin de la jornada ---")