import random

opciones = {"piedra", "papel", "tijera"}
opcion = random.choice(opciones)
usuario = input("ingrese su opcion")
print(opcion)
print(usuario)