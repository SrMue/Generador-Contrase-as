import random
caracters = ('+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
contra = ''
rango = int(input('Que rango desea? '))

for i in range(rango):
    suma = random.choice(caracters)
    contra += suma
print('La contraseña generada es ', contra)

while True:
    sesion = input('Por favor ingrese la contraseña ')
    if sesion == contra:
        print('Contraseña correcta')
        break
    else:
        print('Incorrecta vuelva a intentar')
