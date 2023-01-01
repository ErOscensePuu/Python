num1=int(input("Introduzca el primer número: "))
operador=input("Introduzca un operador(+,-,*,/): ")
num2=int(input("Introduzca el segundo número: "))
if(operador=='+'):
    suma=num1+num2
    print(suma)
elif(operador=='-'):
    resta=num1-num2
    print(resta)
elif(operador=='*'):
    multiplicar=num1*num2
    print(multiplicar)
elif(operador=='/'):
    dividir=num1/num2
    print(dividir)
else:
    print("No has introducido un buen operador")