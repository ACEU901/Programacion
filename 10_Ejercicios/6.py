
print("--- REGISTRO DE COMPRA ---")

categoria_str = input("Ingrese la categoría (ALIMENTOS, TECNOLOGIA, OTROS): ")
monto_float = float(input("Ingrese el monto de la compra: "))
compra = (categoria_str, monto_float)


match compra:
    case ("ALIMENTOS", monto):
        descuento = 0.05
        total = monto - (monto * descuento)
        print(f"Descuento aplicado: 5% (${descuento:.2f})")
        print(f"Total a pagar: ${total:.2f}")
    case ("TECNOLOGIA", monto):
        descuento = 0.10
        total = monto - (monto * descuento)
        print(f"Descuento aplicado: 10% (${descuento:.2f})")
        print(f"Total a pagar: ${total:.2f}")
    case ("OTROS", monto):
        print("Esta categoría no tiene descuento.")
        print(f"Total a pagar: ${monto:.2f}")
    case _:
        print("---- Categoría no reconocida. Verifique si escribió bien 'ALIMENTOS', 'TECNOLOGIA' u 'OTROS'. ---- ")