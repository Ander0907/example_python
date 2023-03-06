# Valor de hora día.
Valor_hora_dia = {
"Diferente" : 5000,
"Tipo A" : 20000,
"Tipo B" : 10000,
}

#Identificamos él valor de la hora día del empleado, para esto se hace:
Horas_laborales_diarias = 8*30

#Luego se hace hace una multiplicacion entre el valor de la hora dia y las horas laborales diarias.
Calculo_sueldo_mensual = Valor_hora_dia["Diferente"] * Horas_laborales_diarias
print("El valor del sueldo mensual es:",Calculo_sueldo_mensual)

#Definimos un tope maximo para el sueldo de cada persona.
tope_maximo = 1500000

# Si Calculo sueldo mensual es >1.500.000, entonces mostrar: “Salario es mayor a tope máximo”
if Calculo_sueldo_mensual > tope_maximo :
    print("Su salario es mayor a tope maximo")
else:
    #Si no, subir el pocentaje en un 6% 
    porcentaje_aumento = 6
    aumento = Valor_hora_dia ["Diferente"] * (porcentaje_aumento / 100)
    valor_con_aumento = Valor_hora_dia ["Diferente"] + aumento 
    print("El valor de hora extra es:", valor_con_aumento)
    Suma = Calculo_sueldo_mensual + valor_con_aumento *3
    print("Su nuevo saldo es:", Suma)