import csv
respuestas = {}
with open("datosdechat.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)