import csv

FILE = "capitales.csv"

las_capitales = []

with open(FILE, 'r', encoding='utf-8') as archivo:  
  lector = FILE.reader(archivo)                       
  for fila in lector:                                
    las_capitales.append(fila)

print(las_capitales) 