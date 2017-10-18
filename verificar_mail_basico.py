# verificacion de imail

mail = input('ingresa tu email: ')
tamaño = len(mail)


for i in mail:
    if i.contains('@') and i.contains('.com'):
        print('te registraste')
    else:
        print('el email es incorrecto')


