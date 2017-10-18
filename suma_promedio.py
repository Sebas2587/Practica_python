# Realizar un programa que lea cuatro valores numéricos e informar su suma y promedio.

a,b,c,d = int(input('numero1:\n')),int(input('numero2:\n')),int(input('numero3:\n')),int(input('numero4:\n'))

#calculamos la suma
suma = a + b + c + d
#calculamos el promedio
promedio = round((suma) / 4)

print('la suma de los numeros es: ', suma, 'y el promedio es: ', promedio)
