#pregunta tamaño lista
#ingresar uno a uno los elementos de la lista
aprendices = []
nota1 = []
nota2 = []
nota3 = []
defi = []
tamano = int(input("ingrese el tamaño de la lista:"))
for i in range(tamano):
   estudiante= input("ingrese el nombre de el estudiante")
   n1 = float(input("ingrese la nota 1:"))
   n2 = float(input("ingrese la nota 2:"))
   n3 = float(input("ingrese la nota 3:"))
   definitiva = (n1+n2+n3)/3
   aprendices. append(estudiante)
   nota1.append(n1)
   nota2.append(n2)
   nota3.append(n3)
   defi.append(definitiva)
   
   
i=0

while i<len(defi):
    print( aprendices[i], defi(i), nota1(i))
    i+=1