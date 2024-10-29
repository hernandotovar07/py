lista = ["pregunta 1", "pregunta 2", "pregunta 3"]
#nos gaurde las repuestas 1 2 y 3
while True:
    pregunta = input(f"ingresa tu pregunta")
    if pregunta == "clima":
     print(f"el clima para hoy es caluroso")
    elif pregunta =="trafico":
     print(f"el trafico esta pesado")
    elif pregunta == "salir":
         print("saliste")
         break
    else:
     print("no entiendo su pregunta")
    
while True:
    pregunta =input(f"ingresa tu 2 pregunta")
    if pregunta =="comida":
        print(f"el almuerzo de hoy fue bandeja paisa")
    elif pregunta =="agua":
        print(f"hoy quitaran el agua")
    elif pregunta == "salir":
        print("saliste")
        break
    else:
        print("no entiendo su pregunta")

        