edad = int(input("ingrese su edad"))
licencia = int(input("tienes licencia (si/no)"))
#validacion
if edad >= 18 and licencia == "si":
   print("pude conducir")
elif edad <= 18 and licencia == "no":
    print("debe sacar licencia")
else:
    print("no puede conducir")
  
