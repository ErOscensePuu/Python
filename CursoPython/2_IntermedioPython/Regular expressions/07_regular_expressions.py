### Regular Expressions ### Ver Hector de leon

import re

my_string = "Esta es la lección número 7:Lección llamada Expresiones Regulares"

my_other_string = "Esta no es la lección número 6:\nManejo de Ficheros"

# match

print(re.match("Esta es la lección", my_string, re.I))
print(re.match("Expresiones Regulares", my_string))#Empieza desde el principio
match=re.match("Esta es la lección", my_string, re.I)
if match is not None:
    print(match)
    span=match.span()
    print(span)
    start, end=match.span()
    print(my_string[start:end])

match=print(re.match("Esta es la lección", my_other_string))
#if match != None: #Otra manera
#if not(match == None):
if match is not None:
    print(match)
    start, end=match.span()
    print(my_other_string[start:end])

# search

search = re.search("lección", my_string, re.I)#No desde el pricipio
print(search)
start, end = search.span()
print(my_string[start:end])# Solo la primera vez

# findall

findall = re.findall("lección", my_string, re.I)# El re.I hace que no diferencía entre mayusculas y minusculas
print(findall)# Te sale cuantas veces aparece la palabra

#split

print(re.split("\n", my_other_string))
print(re.split(":", my_string))

# sub

print(re.sub("Expresiones", "expresiones", my_string))
print(re.sub("lección", "LECCIÓN", my_string))
print(re.sub("lección|Lección", "LECCIÓN", my_string))
print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Patterns

pattern = r"[l|L]ección"
print(re.findall(pattern, my_string))

pattern = r"[l|L]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[a-z]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"[1-9]"
print(re.findall(pattern, my_string))
print(re.match(pattern, my_string))
print(re.search(pattern, my_string))

pattern= r"\d"
print(re.findall(pattern, my_string))

pattern=r"\D"
print(re.findall(pattern, my_string))

pattern= r"[l]."
print(re.findall(pattern, my_string))

pattern= r"[l].*"
print(re.findall(pattern, my_string))

#email validation regular expression (regex)

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"#El dolar significa que cuenta todo lo que tenga detras del punto
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev"
print(re.findall(pattern, email))#No es un gmail porque no cumple el patron no tiene un punto

email = "mouredev@mouredev."#No es un gmail porque no cumple el patron no tiene nada despues del punto
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))



