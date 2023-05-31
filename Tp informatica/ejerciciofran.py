#Pido dos numeros
num1 = int(input('Ingrese un numero: '))
num2 = int (input('Ingrese un segundo numero: '))
#Pido otro numero
num3 = int(input('Ingrese un tercer numero: '))

if num1 > num2:
    if num3 >= num2 and num3 <= num1:
        print(True)
    else:
        print(False) 
elif num2 > num1:
    if num3 <= num2 and num3 >= num1:
        print(True)
    else:
        print (False)