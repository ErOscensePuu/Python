### Higher Order Funcionts ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_two_values_and_add_one(frist_value, seconde_value):
    return sum_one(frist_value + seconde_value)

print(sum_two_values_and_add_one(5,2))

def sum_one(value):
    return value + 1

def sum_five(value):
    return value+5

def sum_two_values_and_add_one(frist_value, seconde_value, f_sum):#Pasamos por parametro la función
    return f_sum(frist_value + seconde_value)

print(sum_two_values_and_add_one(5,2, sum_one))
print(sum_two_values_and_add_one(5,2, sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure)#Esta almacenando una función
print(add_closure(5))

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add
add_closure= sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(3))#El 5 es el original_value y el 1 el value

### Built-in Higher Order Funcions ###

numbers =[5,2,10,21,3,30]

# Map

def multipy_two(number):
    return number * 2

print(map(multipy_two, numbers))# map object at 0x000002301CCCC6A0

print(list(map(multipy_two, numbers)))#Lo pasamos a una lista y la imprimimos

print(list(map(lambda number: number * 3, numbers)))#Con una lambda

# Filter

def filter_greater_that_ten(number):
    if(number>10):
        return True
    return False
    

print(filter(filter_greater_that_ten, numbers))# filter object at 0x00000281757FC6A0
print(list(filter(filter_greater_that_ten, numbers)))

print(list(filter(lambda number: number>10 , numbers)))

# Reduce
# Hay que importarla

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers))

