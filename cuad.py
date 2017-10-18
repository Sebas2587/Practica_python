'''programa para calcular cuadradod e numeros'''

def main():
    print('se calcularan cuadrados de numeros')
    n1 = int(input('ingrese un numero entero: '))
    n2 = int(input('ingrese otro numero entero: '))
    print('se muestra el numero con su respectivo cuadrado')
    for x in range(n1, n2):
        nom_cuad = x
        
        print('numero: ',nom_cuad, '--> ','su cuadrado: ',x*x)
    print('es todo')


main()
