# Ingreso de datos del alumno
curso = int(input("Ingrese su año de curso: "))
arancel = input("¿Tiene el arancel pagado? (si/no): ").strip().lower()
suspendido = input("¿Está suspendido? (si/no): ").strip().lower()
#NOTA :) .strip().lower() PARA MAYUSCULAS
# .strip() — elimina espacios accidentales: " Si " → "Si" MAYUSCULAS

#
# Validación de condiciones
if curso >= 2 and arancel == "si" and suspendido == "no":
    print("Acceso: PERMITIDO")
else:
    print("Acceso: DENEGADO")
    if curso < 2:
        print("- Motivo: debe estar cursando 2do año o superior")
    if arancel != "si":
        print("- Motivo: debe tener el arancel pagado")
    if suspendido != "no":
        print("- Motivo: no debe estar suspendido")
