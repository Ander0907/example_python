#En este codigo, veremos los datos y aumento del IVA en una factura de un mercado 

datos_persona = {
    
    "Nombre" : "Andres",
    "Cedula" : 33548923,
    "Direccion" : "Cll 96bb #81-68",
    "Telefono" : 4334581
    }
    
print(datos_persona)


precio_productos = {
    "Arroz x 5lb" : 20000,
    "Carne x 5lb" : 35000,
    "Papa x 2K" : 18000,
    "Salsa" : 1500,
    "Gaseosa" : 2000,
    "Sal x 1lb" : 3000,
    "Frijol x 5lb" : 16000,
    "Lentejas x 5lb" : 16000,
    "Aceite" : 5000,
    "Jabon liquido" : 8000,
    "Papel higenico" : 16000,
    "Leche x 12" : 32000
}
print(precio_productos)
price = precio_productos ["Arroz x 5lb"] + precio_productos ["Carne x 5lb"] + precio_productos ["Papa x 2K"] + precio_productos ["Salsa"] + precio_productos ["Gaseosa"] + precio_productos["Sal x 1lb"] + precio_productos["Frijol x 5lb"] + precio_productos["Lentejas x 5lb"] + precio_productos["Aceite"] + precio_productos ["Jabon liquido"] + precio_productos["Papel higenico"] + precio_productos ["Leche x 12"]
print("Total:",price)


#Incremento del iva
porcentaje_aumento = 10.00
aumento = price * (porcentaje_aumento / 100)
valor_con_aumento = price + aumento
print("El valor con aumento es:", valor_con_aumento)




