### File Handling ###

import os

# .txt file
"""
txt_file= open("CursoPython/2_IntermedioPython/my_file.txt","w+")
txt_file= open("CursoPython/2_IntermedioPython/my_file.txt","r+")#Leer y Escribir
print(txt_file.read())#Le todo el fichero
print(txt_file.read(10))#Printea los diez siguientes caracteres
print(txt_file.readline())#Le la siguiente linea dejando una espacio
print(txt_file.readline())
print(txt_file.readlines())#Te mete todo en un array de Strings linea por linea
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Java")#Te lo escribe en la ultima línea del fichero
print(txt_file.readline())

txt_file.close()#Cierro el fichero

os.remove("CursoPython/2_IntermedioPython/my_file.txt") #Elimino el fichero
"""

#CUANDO NO TENGO EL FICHERO CREO UNO ESCRIBO EN EL, LUEGO LO CIERRO
txt_file= open("CursoPython/2_IntermedioPython/my_file.txt","w+")#Leer y Escribir y sobreescribir si ya existe

txt_file.write("Mi nombre es Pascual\nMi apellido es Ferrer\n19 años\nY mi lenguaje preferido")
#Para poder leerlo hay que cerrarlo
txt_file.close()
txt_file= open("CursoPython/2_IntermedioPython/my_file.txt","r+")
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Java")#Te lo escribe en la ultima línea del fichero
print(txt_file.readline())

txt_file.close()#Cierro el fichero

with open("CursoPython/2_IntermedioPython/my_file.txt","a") as my_other_file:
    my_other_file.write("\nY c")

# .json file

import json

json_file = open("CursoPython/2_IntermedioPython/my_file.json","w+")

json_test = {
    "name":"Pascual",
    "surname":"Ferrer", 
    "age":18, 
    "Lenguajes":["Python","Java","c"],
    "website":"https://moure.dev"}

#json.dump(json_test,json_file, indent=0)#Tiene 0 espacios
json.dump(json_test,json_file, indent=2)#Tiene 2 espacios

json_file.close()

json_file = open("CursoPython/2_IntermedioPython/my_file.json","r+")

with open("CursoPython/2_IntermedioPython/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("CursoPython/2_IntermedioPython/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
print(len(json_dict))

# .csv file

import csv

csv_file = open("CursoPython/2_IntermedioPython/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Keys","name", "surname", "age", "language", "website"])
csv_writer.writerow(["Value","Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

#with open("Intermediate/my_file.csv") as my_other_file:
 #   for line in my_other_file.readlines():
 #       print(line)

# .slsx file

#import xlrd # Debe instalarse el módulo

# .xml file

import xml
