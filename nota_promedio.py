# Se ingresan tres notas de un alumno, si el promedio
# es mayor o igual a siete mostrar un mensaje "Promocionado".

print('ingresar notas del alumno')
nota1, nota2, nota3, nota4 = float(input('nota1: ')),float(input('nota2: ')),float(input('nota3: ')),float(input('nota4: '))

promedio = (nota1 + nota2 + nota3 + nota4) / 4

if promedio >= 7:
    print('Nota: ', promedio, '\n', 'Promocionado')
else:
    print('repitente del curso con Nota:', float(promedio))
