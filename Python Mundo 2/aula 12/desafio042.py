print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulos')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')

if r1 == r2 and r2 == r3:
    print('Seu triângulo é um EQUILÁTERO')
elif r1 == r2 or r2 == r3 or r1 == r3:
    print('Seu triângulo é um Isósceles')
else:
    print('Seu triângulo é um Escaleno')