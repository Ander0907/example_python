Valor_hora_dia = {
"Diferente" : 5000,
"Tipo A" : 20000,
"Tipo B" : 10000,
}

Horas_laborales_diarias = 8*30
Calculo_sueldo_mensual = Valor_hora_dia["Diferente"] * Horas_laborales_diarias
print("El valor del sueldo mensual es:",Calculo_sueldo_mensual)
tope_maximo = 1500000
if Calculo_sueldo_mensual > tope_maximo :
    print("Su salario es mayor a tope maximo")
else: 
    porcentaje_aumento = 6
    aumento = Valor_hora_dia ["Diferente"] * (porcentaje_aumento / 100)
    valor_con_aumento = Valor_hora_dia ["Diferente"] + aumento 
    print("El valor de hora extra es:", valor_con_aumento)
    Suma = Calculo_sueldo_mensual + valor_con_aumento *3
    print("Su nuevo saldo es:", Suma)