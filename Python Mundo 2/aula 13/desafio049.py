num = int(input('Digite um número para saber sua tabuada: '))
for c in range (1,11):
    print('{} X {:2} = {}'.format(num, c, num*c))