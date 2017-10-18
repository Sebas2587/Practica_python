'''Leer cuántas millas tiene la longitud dada
y referenciarlo con la variable millas)

Leer cuántos pies tiene la longitud dada
(y referenciarlo con la variable pies)
 
Leer cuántas pulgadas tiene la longitud dada
(y referenciarlo con la variable pulgadas)
 
Calcular metros = 1609.344 * millas +
    0.3048 * pies + 0.0254 * pulgadas
 
Mostrar por pantalla la variable metros'''

print('convierte medidas inglesas a sistema metrico')
milla = int(input('ingresa las millas: '))
pie = int(input('ingresa los pies: '))
pulgada = int(input('ingresa las pulgadas: '))

longitud = lambda m, p, pu: (609.344 * int(m)) + (0.3048 * int(p))+ (0.0254 * int(pu))
print('la longitud es: ', longitud(milla, pie, pulgada), ' metros')
