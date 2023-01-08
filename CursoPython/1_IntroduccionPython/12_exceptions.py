### Exceptions Handling###

numberOne,numberTwo=5,1
numberTwo="1"

#try except
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    #Se ejecuta si se produce una exceptión
    print("Se ha producido un error")

#Tye except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #Se ejecuta  si no se produce una excecpción
    print("La ejecución continúa correctamente")

#Try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    #Se ejecuta aun si ocurre una excepción como si no
    print("La ejecución continúa")

#Exception por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    #Se ejecuta si se procude un error de tipo ValueError
    print("Se ha producido un ValueError")
except TypeError:
    #Se ejecuta si se procude un error de tipo ValueError
    print("Se ha producido un TypeError")


#Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as e:
    #Te captura que ha producido el error
    print(e)
except Exception as e:
    #Te captura cualquier exception
    print(e)
finally:
    print("Eres inutil")