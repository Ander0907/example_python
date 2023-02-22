#Productos
nombres = {
    "Zapatos" : 350000,
    "Tenis" : 280000,
    "Camisetas" : 175000,
    "Jeans" : 200000
}
print(nombres)

#Total
price = 1005000
print("Total:", price)

#Promedio de venta
num1 = 350000
num2 = 280000
num3 = 175000
num4 = 200000
sumar = num1 + num2 + num3 + num4
cantidad = 4
promedio = sumar / cantidad
print(f"El promedio es:", promedio)

#Subir el precio de los Jeans en un 6.2%
porcentaje_aumento = 6.2
valor_original = 200000
aumento = valor_original * (porcentaje_aumento / 100)
valor_con_aumento = valor_original + aumento
print(f"El valor con aumento es: {valor_con_aumento}")

#Disminuir el precio de los Zapatos en un 0.8%
porcentaje_aumento2 = 0.8
valor_original2 = 350000
descuento= valor_original2 * (porcentaje_aumento2/100)
valor_con_descuento= valor_original2 - porcentaje_aumento2
print(f"El valor con disminucion es: {valor_con_descuento}")
