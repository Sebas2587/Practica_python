'''programa para saludar a usuario y mostrar producto de 2 numeros'''

nombre = input('por favor, dime tu nombre: ')
print(nombre, 'ingresa 2 numeros')

n1 = int(input('\n'))
n2 = int(input())

producto = n1 / n2

print(nombre, 'el producto de los numeros', n1, n2,'es: ', producto)
