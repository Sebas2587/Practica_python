

def suma(a, b):
    return int(a) + int(b)

def resta(a, b):
    return int(a) - int(b)

def multiplicacion(a, b):
    return int(a) * int(b)

def division(a, b):
    return int(a) / int(b)


print('calculadora')
print('selecciona una opcion...')
print('selecciona: 1,2,2,3,4')

choice = input()

if choice == '1':
    print('suma')
    num1 = input()
    num2 = input()
    print('la suma de los numeros es: ', suma(num1, num2))
elif choice == '2':
    print('resta')
    num1 = input()
    num2 = input()
    print('la resta de los numeros es: ', resta(num1, num2))
elif choice == '3':
    print('mltiplicacion')
    num1 = input()
    num2 = input()
    print('la multiplicacion de los numeros es: ', multiplicacion(num1, num2))
elif choice == '4':
    print('division')
    num1 = input()
    num2 = input()
    print('la division de los numeros es: ', division(num1, num2))
else:
    print('la opcion que ingresaste no es valida')

