print("--- Calculadora de Costo Total ---")

while True:
    nombre_producto = input("Ingrese el nombre del producto: ")
    if nombre_producto.isalpha():
        break
    else:
        print("El nombre del producto debe contener solo letras.")
while True:
    try:
        precio_unitario = float(input("Ingrese el precio unitario del producto: "))
        if precio_unitario > 0:
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
        descuento_porcentaje = float(input("Ingrese el porcentaje de descuento (0-100, o deje en blanco si no hay descuento): ") or 0)
        if 0 <= descuento_porcentaje <= 100:
            break
        else:
            print("El porcentaje de descuento debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número para el descuento.")

costo_sin_descuento = precio_unitario * cantidad
monto_descuento = costo_sin_descuento * (descuento_porcentaje / 100)
costo_total = costo_sin_descuento - monto_descuento

print("\n--- Resumen de la compra ---")
print(f"Producto: {nombre_producto}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Cantidad: {cantidad}")
print(f"Descuento aplicado: {descuento_porcentaje:.2f}%")
print(f"Costo total: ${costo_total:.2f}")