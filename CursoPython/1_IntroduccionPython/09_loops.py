### Bucles ###

# While

my_condition=0

while my_condition<10:
    print(my_condition)
    my_condition +=1#Incremeta de 1 en uno
else:#El esle pertenece al while y es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition<20:
    my_condition+=1
    if my_condition==15:
        print("Mi condición es 15")
        break

    print(my_condition)

    #For

my_list =[32,24,18,16,15,60,52]

for element in my_list:
    print(element)

my_tuple=(35,1.77,"Pascual","Ferrer","Puu")

for element in my_tuple:
    print(element)

my_set={"Pascual","Ferrer",18}

for element in my_set:
    print(element)

my_dict={"Nombre":"Pascual", "Apellido":"Ferrer", "Edad":18, 1:"Python"}

for element in my_dict:
    print(element)

for element in my_dict.values():
    print(element)
    if element ==18:
        break
else:
    print("El bulce for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict.values():
    print(element)
    if element ==18:
        continue#Que siga para adelante pero empezando desde el for
    print("Se ejecuta")#Cuando llega a 18 no se ejecuta por el continue
else:
    print("El bulce for para diccionario ha finalizado")

print("La ejecución continúa")


