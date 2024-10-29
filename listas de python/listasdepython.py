#pregunta tamaño lista
#ingresar uno a uno los elementos de la lista
lista = []
tamano = int(input("ingrese el tamaño de la lista"))
while tamano !=0:
   valor= input("ingrese el elemento de la lista")
   lista.append(valor)
   tamano -=1
i=0

lista.append(11)
#print(len(lista))
while i<len(lista):
    print(lista[i])
    i+=1

