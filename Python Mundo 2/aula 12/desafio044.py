preco = float(input('Digite o valor do produto: R$'))
din_che = preco - (preco*0.10)
c1x = preco - (preco*0.05)
c3x = preco + (preco*0.20)
pagamento = int(input('Escolha a forma de pagamento: \n1 - À vista dinhero/cheque \n2 - À vista cartão \n3 - 2x no cartão \n4 - 3x ou mais no cartão \n '))

if pagamento == 1:
    print('O valor ficará R${:.2f}!'.format(din_che))
elif pagamento == 2:
    print('O valor ficará R${:.2f}!'.format(c1x))
elif pagamento == 3:
    print('O valor ficará R${:.2f}!'.format(preco))
elif pagamento == 4:
    print('O valor ficará R${:.2f}!'.format(c3x))
else:
    print('Forma de pagamento inválida!')