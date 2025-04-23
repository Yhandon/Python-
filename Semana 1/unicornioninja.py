print("UNICORNIO NINJA")

edad = int(input("ingrese su edad:"))
PaseDorado= input("¿Tienes pase dorado? si/no:")

#Reglas
if edad <= 17:
    print("No puedes entrar")
elif PaseDorado == "si":
    print("Puedes entrar")
elif edad > 17 and edad <= 25 and PaseDorado == "no":
    print("Puedes entrar")
elif edad > 25:
    print("no puedes entrar")
