nombre = input("ingresa el nombre de tu mascota")
peso = float(input("ingresa el peso de tu mascota"))
catodog = print("tu mascota es un perro o gato?")



#clasificacion

if catodog == "perro" and peso < 10:
     print("consulta pequeña (15.OOO)")
    elif catodog == "perro" and peso >= 10:
     print("consulta grande (22.000)" )
     elif catodog == "gato":
     print("consulta felina 12.000")
else:
     print("especie no atendida em esta clinica")
