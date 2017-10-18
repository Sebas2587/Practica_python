#camculadora lambda

print('***********************calculadora lambda**************')
print('*************************************++++++++++++++++++')


#suma lambda


while True:
    opcion = input('ingresa un opcion: ')
    if opcion > '0' or opcion <= '4':
        if opcion == '1':
            num1 = input('ingresa un numero para sumar: ')
            num2 = input('ingresa otro numero para sumar: ')
            suma = lambda n1, n2: int(n1) + int(n2)
            print('la suma de los numeros es: ',  suma(num1,num2))
            continue
        elif opcion == '2':
            num1 = input('ingresa un numero para restar: ')
            num2 = input('ingresa otro numero para restar: ')
            resta = lambda n1, n2: int(n1) - int(n2)
            print('la suma de los numeros es: ',  resta(num1,num2))
            continue
        elif opcion == '3':
            num1 = input('ingresa un numero para multiplicar: ')
            num2 = input('ingresa otro numero para multiplicar: ')
            multi = lambda n1, n2: int(n1) * int(n2)
            print('la multiplicaicon de los numeros es: ',  multi(num1,num2))
            continue
        elif opcion == '4':
            num1 = input('ingresa un numero para dividir: ')
            num2 = input('ingresa otro numero para dividir: ')
            div = lambda n1, n2: int(n1) / int(n2)
            print('la multiplicaicon de los numeros es: ',  div(num1,num2))
