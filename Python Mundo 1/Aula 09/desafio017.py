from math import sqrt

co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hn2 = (co**2)+(ca**2)
hn = sqrt(hn2)

print('A hipotenusa é igual a: {}'.format(hn))