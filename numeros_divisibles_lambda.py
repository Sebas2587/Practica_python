'''programa ara encontrar los numeros divisibles
    usando funciones anonimas'''


divisible = int(input('ingresa un divisible'))
lista = [12, 65, 54, 39, 102, 339, 221,]
resultado = list(filter(lambda x: (x % divisible == 0),lista))

print("numeros divisibles por: " , divisible, "son: ", resultado)
