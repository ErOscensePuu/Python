###Tuples###

my_tuple=tuple()
my_other_tuple=()

my_tuple=(18,1.78,"Pascual","Ferrer","Puu")
my_other_tuple=(35,60,30)

print(my_tuple)
print(type(my_tuple))


print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-5]) IndexError

print(my_tuple.count("Ferrer"))
print(my_tuple.index("Pascual"))
"""
my_tuple[1]=1.80
print(my_tuple)
No se puede cambiar los valores son inmutables
"""

my_sum_tuple=my_tuple+my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple=list(my_tuple)
print(type(my_tuple))

my_tuple[4]="Pascualfo"
my_tuple.insert(1, "Azul")
my_tuple=tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))
print(len(my_sum_tuple))

del my_tuple
#print(my_tuple)NameError. name 'my_tuple' is not defined
