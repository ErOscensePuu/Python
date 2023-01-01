#Así es lo mejor para hacer una variable con muchos nombres
my_string_variable="My String variable"
print(my_string_variable)

my_int_variable=5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(type(my_int_to_str_variable))

my_bool_variable=False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable,my_int_variable, my_bool_variable)
print("Es es el valor de:",my_bool_variable)

#Funciones del sistema
print(len(my_string_variable))#lo que haces es un .length()

#Variables es una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age="Pascual","Ferrer", "Pu",18
print("My llamo:",name,surname,"Mi edad es:", age,"Y mi alias es:", alias)

#Forzamos el tipo
address: str="Mi dirección"
edad:int=15