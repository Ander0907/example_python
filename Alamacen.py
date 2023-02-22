#Productos
precio_productos = {
    "Zapatos" : 350000,
    "Tenis" : 280000,
    "Camisetas" : 175000,
    "Jeans" : 200000
}
print(precio_productos)

#Total
price = precio_productos["Camisetas"] + precio_productos["Jeans"] + precio_productos["Tenis"] + precio_productos["Zapatos"]
print("Total:", price)

#Promedio de venta
promedio = price / 4
print("El promedio es:", promedio)

#Subir el precio de los Jeans en un 6.2%
porcentaje_aumento = 6.2
aumento = precio_productos["Jeans"] * (porcentaje_aumento / 100)
valor_con_aumento = precio_productos["Jeans"] + aumento
print("El valor con aumento es:", valor_con_aumento)

#Disminuir el precio de los Zapatos en un 0.8%
porcentaje_disminucion = 0.8
disminucion = precio_productos["Zapatos"] * (porcentaje_disminucion/100)
precio_total=  precio_productos["Zapatos"] - disminucion
print("El valor con disminucion es:", precio_total)
