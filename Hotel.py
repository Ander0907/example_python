#Tarifas del hotelWC 
categoría = { 
    "individual" : 2500 , 
    "doble" : 4600 ,
    "familiar" : 5200 ,
    }
print( categoría )
 #Proceso de hospedaje 
dia = 4
precio = dia * categoría[ "individual" ]
print ( "Su categoria es individual:" )
print ( "Su valor total por sus dias de hospedaje es:" , precio )

 #Valor con iva
iva = 16 
aumentar = precio * ( iva / 100 )
aumentado = precio + aumentar 
print ( "Nuevo valor con iva:" ) 
print (aumentado) 

#Descuento con iva
descuento = 5 
print ( "Se te hara un descuento del 5%:" ) 
proceso = aumentado * ( descuento / 100 ) 
disminucion = aumentado - proceso 
print ( "Valor con descuento:" )
print ( disminucion )