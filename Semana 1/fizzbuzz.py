num= int (input("ingrese un numero:"))

resultado =""
if num % 3== 0 and num %5==0:
    resultado+="fizz buzz"
elif num % 5==0:
    resultado+="buzz"
elif num % 3==0:
    resultado+="fizz "
if not resultado:
    resultado = str(num)
print(resultado)
    

    

