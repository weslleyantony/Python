import random
print('-='*20)
print('JOKENPÔ com PYTHON')
print('-='*20)

escolha = int(input('''Escolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
'''))
sorteio = random.randint(1,3)


print('Você escolheu {}'.format(escolha))

if sorteio == 1:
    print('A IA escolheu PEDRA')
elif sorteio == 2:
    print('A IA escolheu PAPEL')
else:
    print('A IA escolheu TESOURA')

if sorteio == 1 and escolha == 'PEDRA':
    print('O JOGO EMPATOU!')
elif sorteio == 2 and escolha == 'PEDRA':
    print('VOCÊ PERDEU!')
elif sorteio == 3 and escolha == 'PEDRA':
    print('VOCÊ GANHOU!')
elif sorteio == 1 and escolha == 'PAPEL':
    print('VOCÊ GANHOU!')
elif sorteio == 2 and escolha == 'PAPEL':
    print('O JOGO EMPATOU!')
elif sorteio == 3 and escolha == 'PAPEL':
    print('VOCÊ PERDEU!')
elif sorteio == 1 and escolha == 'TESOURA':
    print('VOCÊ PERDEU!')
elif sorteio == 2 and escolha == 'TESOURA':
    print('VOCÊ GANHOU!')
elif sorteio == 3 and escolha == 'TESOURA':
    print('O JOGO EMPATOU!')
