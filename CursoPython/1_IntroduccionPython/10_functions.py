### Functions ###

def my_funcion():#Creas la función
    print("Esto es una función")

my_funcion()#Llamas la función

def sum_two_numbers(first_number, second_number):
    if first_number.isnumeric()==True and second_number.isnumeric()==True:
        num1=int(first_number)
        num2=int(second_number)
        print(num1+num2)
    else:
        print("No son numeros enteros")
num1="5"
num2="8"

sum_two_numbers("15","2")
sum_two_numbers(num1,num2)
sum_two_numbers("515154","866932")

def sum_two_values_with_return(first_values,second_values):
    my_sum=first_values+second_values
    return my_sum

my_result = sum_two_values_with_return(10,5)
print(my_result)

def sum_two_values_with_return_print(first_values,second_values):
    my_sum=first_values+second_values
    return print(my_sum)

my_result_print=sum_two_values_with_return_print(12,6)
print(my_result_print)#Te pone none porque no hay nada guardado en un print

def print_name(name,surname):
    print(f"{name} {surname}")

print_name("Pascual","Ferrer")

print_name(surname="Ferrer",name="Pascual")
"""
nombre=input("Introduzca tu nombre: ")
apellido=input("Introduzca tu apellido: ")
print_name(nombre,apellido)
"""
def print_name_with_default(name,surname,alias="Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Pascual","Ferrer","Puu")
print_name_with_default("Pascual","Ferrer")

def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_upper_texts("Hola","Python","Puu")
print_upper_texts("Hola")
