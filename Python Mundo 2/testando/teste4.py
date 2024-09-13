comeco = int(input('Em que número começa? '))
final = int(input('Em que número acaba? '))
intervalo = int(input('Qual o intervalo? '))

for cont in range (comeco, final+1, intervalo):
    print(cont)