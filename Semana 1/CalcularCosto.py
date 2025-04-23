



print("costo total")

while True:
    nombreproducto= input("ingrese el nombre del producto:")
    if nombreproducto.isalpha(): # se utiliza es .isalpha para comprobar que los datos que se ingresan solo sean letras
        break 
    else:
        print("El nombre del producto debe contener solo letras.")


while True:
    try:
        preciounidad= float(input("Ingrese el precio unitario del producto: "))
        if preciounidad > 0:
            break
        else:
            print("El precio unitario debe ser un número positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el precio.")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos adquiridos: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser un número entero positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero para la cantidad.")

while True:
    try:
        descuentoporcentaje = float(input("Ingrese el porcentaje de descuento (0-100, o deje en blanco si no hay descuento): ") or 0)
        if 0 <= descuentoporcentaje <= 100:
            break
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el descuento.")

costo_sin_descuento = preciounidad * cantidad
monto_descuento = costo_sin_descuento * (descuentoporcentaje / 100)
costo_total = costo_sin_descuento - monto_descuento


print("\n--- Resumen de la compra ---")
print(f"Producto: {nombreproducto}")
print(f"Precio unitario: ${preciounidad:.2f}") #se utiliza la notacion 2f para redondear a 2 decimales ya que es un punto float
print(f"Cantidad: {cantidad}")
print(f"Descuento aplicado: {descuentoporcentaje:.2f}%")
print(f"Costo total: ${costo_total:.2f}")


#DOCUMENTACION
#https://www.w3schools.com/python/python_try_except.asp
#https://www.freecodecamp.org/espanol/news/2f-en-python-que-significa/
#https://www.w3schools.com/python/python_while_loops.asp
#https://docs.python.org/3/library/exceptions.html