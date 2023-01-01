###Condicionales###

my_condition= False

if my_condition:
    print("Se ejecuta la condición del if")

print("La ejecución continúa")

my_string=""

if my_string:#Si la cadena esta vacía lo toma como false
    print("Mi cadena de texto no es vacía")

my_other_string="Mi cadena de texto"

if my_other_string:
    print("Mi cadena de texto no es vacía")

if my_other_string=="Mi cadena de texto":
    print("Mi cadena de texto no es vacía")

if not my_string:#Niego que mi cadena de texto es vacia
    print("Mi cadena de texto no es vacía")
    