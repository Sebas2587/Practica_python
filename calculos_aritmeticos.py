from math import pi


def perimetro_area_rec():
    print('calculo del perimetro de un rectangulo \n')
    a = int(input('ingresa lado 1'))
    b = int(input('ingresa lado 2'))

    perimetro = (a+b) * 2
    area = a * b
    print('el perimetro del rectangulo con medidas ',a,b,' es: ', perimetro)
    print('el area del rectangulo con medidas ',a,b,' es: ', area)


def perimetro_area_circ():
    print('calculo del area de un circulo \n')
    a = int(input('ingresa el radio del circulo'))
    area = round(pi * a**2, 2)
    perimetro = (pi**2) * 2
    print('el area del circulo con medidas ',a,' es: ', area)
    print('el perimetro del circulo con medidas ',a,' es: ', perimetro)

def volumen_esfera():
    print('calculo del volumen de una esfera \n')
    a = int(input('ingresa el radio de la esfera'))
    volumen = round((4 * pi * a**2) / 3, 3)
    print('el volumen de la esfera con radio ',a,' es: ', volumen)

