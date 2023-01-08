###Diccionarios###

my_dict=dict()
my_other_dict={}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict={"Nombre":"Pascual", "Apellido":"Ferrer", "Edad":18, 1:"Python"}

my_dict={
    "Nombre":"Pascual",
    "Apellido":"Ferrer", 
    "Edad":18, 
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.78
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict["Lenguajes"])

my_dict["Nombre"]="Pedro"
print(my_dict["Nombre"])

#print(my_dict["1"])No funcionara porque hemos puesto que uno es una clave de entero
print(my_dict[1])

my_dict["Calle"]="Calle Calatayud"
print(my_dict)

del my_dict["Calle"]#Para eliminar un elemento en el diccionario
print(my_dict)

#Te mira si esta la clave en el diccionario
print("Ferrer" in my_dict)#False
print("Apellido" in my_dict)#True

print(my_dict.items())#Te saca un listado con las claves y los valores
print(my_dict.keys())#Te un listado de las claves
print(my_dict.values())#Te un listador de los valores

my_list=["Nombre",1, "Piso"]
my_new_dict=dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict=dict.fromkeys(("Nombre",1, "Piso"))
print(my_new_dict)
my_new_dict=dict.fromkeys(my_dict)#Reaprovecha las claves
print(my_new_dict)
#Esto lo que hace es meter "Pascual","Ferrer" a todas las claves
my_new_dict=dict.fromkeys(my_dict,("Pascual","Ferrer"))
print(my_new_dict)

my_values=my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))