import math

ang = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('COm o angulo de {}° temos o seno igual a {:.2f}, cosseno igual a {:.2f} e tangente igual a {:.2f}!'.format(ang,seno,cosseno,tangente))
