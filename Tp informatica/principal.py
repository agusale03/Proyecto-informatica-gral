    
import csv

FILE = "C:\\Users\\agual\\OneDrive\\Escritorio\\Tp informatica\\locales-en-venta-2020.csv"

locales = []

with open(FILE, 'r', encoding='latin-1') as archivo:  
  lector = csv.reader(archivo)                       
  for fila in lector:                                
    locales.append(fila)


print(locales) 
 


from funcionestp import transformacion_de_dato_con_while

print(transformacion_de_dato_con_while(locales[2]))

print(type(locales[2][1]))




     


 



