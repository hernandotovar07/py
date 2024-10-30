def saludar():
   print("hola mundo")

saludar()

def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# Llamar a la función con un argumento
saludar("Ana")  # Imprime "¡Hola, Ana!"


def sumar(a , b):
    return a + b
numero1 = input("ingresar numero 1")
numero2 = input("ingresa numero 2")
resultado = sumar(numero1 + numero2)
print(resultado)



suma = lambda x, y: x + y

resultado = suma(4, 7)
print(resultado)  # Imprime 11