while True:
    saludo = input(
        "BIENVENIDO AL MENU DE SALUDOS:\n"
        "(1) hola\n"
        "(2) alo\n"
        "(3) como estas\n"
        "(4) salir\n"
    )
    nombre = input("Ingresa tu nombre: ")

    if saludo == "1":
        print("hola", nombre)
    # asignacion saludo
    elif saludo == "2":
        print("alo", nombre)
    elif saludo == "3":
        print("cómo estas", nombre)
    elif saludo == "4":
        print("adios :)", nombre)
        break        # ← detiene el while
    else:
        print("gracias por usar :)")
