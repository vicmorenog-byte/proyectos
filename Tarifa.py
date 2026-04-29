# Solicitar datos al usuario
nombre = input("Ingrese el nombre del cliente: ")
tipo_tarifa = input("Ingrese el tipo de tarifa (residencial/comercial): ").strip().lower()
consumo = float(input("Ingrese el consumo en kWh: "))

# Calcular el monto a pagar
if tipo_tarifa == "residencial":
    if consumo <= 150:
        monto = consumo * 82
    else:
        monto = (150 * 82) + ((consumo - 150) * 110)
elif tipo_tarifa == "comercial":
    monto = consumo * 130
else:
    print("Tipo de tarifa no válido.")
    exit()

# Mostrar resultados
print(f"\nNombre del cliente: {nombre.upper()}")
print(f"Largo del nombre: {len(nombre)}")
print(f"Tipo de tarifa: {tipo_tarifa}")
print(f"Consumo: {consumo} kWh")
print(f"Monto a pagar: ${monto:.2f}")
