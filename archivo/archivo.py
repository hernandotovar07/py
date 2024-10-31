import csv

with open("salida.csv", "w", newline="")as archivo:
       escritor = csv.writer(archivo)
       escritor.writerow (["Nombre", "Edad"]) 
       escritor.writerow (["Ana", 28])
       escritor. writerow (["Luis", 35])