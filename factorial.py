

def factorial(x):
    '''calculo de factorial
        con una funcion recursiva'''
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 928

print('el factorial de: ', num ,'is ', factorial(num))
