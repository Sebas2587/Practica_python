# Calcular el sueldo mensual de un operario conociendo
# la cantidad de horas trabajadas y el valor por hora

hora_trabajada = int(input('ingresa cantidad de horas trabajadas: '))

dias_trabajados = int(input('ingresa cantidad de dias trabajados: '))

valor_hora = 2500

print('sueldo trabajador: ', (valor_hora * hora_trabajada) * dias_trabajados)
