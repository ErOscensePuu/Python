name, surname, age="Pascual","Ferrer",18
#Diferentes maneras del print con variables
print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))#Como en c
print("Mi nombre es "+name+" "+surname+" y mi edad es "+str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#Desempaquetado de caracteres
language="python"
a, b, c, d, e, f =language
print(a)
print(e)

#División

language_slice=language[1:3]
print(language_slice)
language_slice=language[1:]
print(language_slice)
language_slice=language[-2]
print(language_slice)

#Reverse

reversed_language=language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())#Primera letra en mayuscula
print(language.upper())#Toda la palabra en mayuscula
print(language.count("t"))#Cuenta las t en la palabra
print(language.isnumeric())#Si es un número
print("1".isnumeric())
print(language.lower())#Te pone todas en minuscula
print(language.upper().isupper())#Te dice si esta en mayuscula o no
print(language.islower())#Si esta en minusculas o no
print(language.startswith("py"))#Te dice si la python empieza por py