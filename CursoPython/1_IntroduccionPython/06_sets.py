###Sets###

my_set=set()
my_other_set={}

print(type(my_set))
print(type(my_other_set))#Inicialmente es un diccionario

my_other_set={"Pascual","Ferrer",18}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Puu")

print(my_other_set)#Un set no es una estructura ordenada

my_other_set.add("Puu")#Un set no admite repetidos

print(my_other_set)

print("Ferrer" in my_other_set)#Mira si esta en el set
print("Pascualfo" in my_other_set)

my_other_set.remove("Puu")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))
print(my_other_set)

del my_other_set
#print(my_other_set)NameError:name 'my_other_set' is not defined

my_set={"Pascual","Ferrer",18}
my_list=list(my_set)
print(my_list)
print(my_list[0])#Es arriesgado ya que no sabemos el orden de la lista

my_other_set={"Kotlin","Swift","Python"}

my_new_set=my_set.union(my_other_set)#Uno dos set
print(my_new_set.union({"JavaScript","c#"}))

print(my_new_set.difference(my_set))#Quitamos los elementos de my_set
