pre1="" 
while pre1!="si" and pre1!="no":
    pre1=input("¿Estas bien? ")
if(pre1=="si"):
    pre2=""
    while pre2!="si" and pre2!="no":
        pre2=input("¿Has ganado en algo? ")
    if(pre2=="si"):
        print("Me alegro")
    else:
        print("Entoces de chill")
else:
    pre3=""
    while pre3!="si" and pre3!="no":
        pre3=input("¿Has perdido algo? ")
    if(pre3=="si"):
            print("Pobrecillo")
    else:
        print("Entoces de chill")