import time

print('=-'*20)
print('Contagem Regressiva')
print('=-'*20)

segundos = int(input('Quantos segundos? '))

for intervalo in range (segundos, 0, -1):
    print(intervalo)
    time.sleep(1)
print('FIM!')