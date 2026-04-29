anos = print("cuantos años ties de experiencia?")
nivel = len(print("ingrese su nivel de ingles"))
dispo = print("disponible para viajar?")

#menu
if años >= 5:
    print("postulante avanzado pasa a entrevista final")

if años > 3 and nivel == "avanzado" :
    print("ingles intermedio OR avanzado pasa a seg2 fase")

elif  dispo == "si" and años >= 1 :
    print("postulante en revision")

else:
    print("postulante no cumple con requisitos")

