### Classes ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Name:
    def __init__(self,name,surname):
        self.name =name
        self.surname= surname
my_person = Name("Pascual","Ferrer")

class MyName:
    def __init__(self):
        self.alias ="Puu"
        self.edad= 18
my_person2= MyName()
print(f"Soy {my_person.name} {my_person.surname} y mi alias es {my_person2.alias} y tengo {my_person2.edad}")

class Person:
    def __init__(self,name,surname):
        self.full_name= f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está caminando")
    

my_person=Person("Pascual", "Ferrer")
print(my_person.full_name)
my_person.walk()

class MyPerson:
    def __init__(self,name,surname,alias="Sin alias"):
        self.full_name= f"{name} {surname} ({alias})"#Propiedad publica
        self.__name=name#Propiedad privada
        self.__surname=surname
    
    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")

my_person=MyPerson("Pascual", "Ferrer")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person=MyPerson("Pascual","Ferrer","Puu")
print(my_other_person.full_name)
print(type(my_other_person.full_name))
my_other_person.walk()
my_other_person.full_name="Héctor de León (El loco de los perros)"
print(my_other_person.full_name)
my_other_person.full_name=1
print(my_other_person.full_name)
