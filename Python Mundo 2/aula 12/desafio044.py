print('{:=^40}'.format(' LOJAS SILVA '))
preco = float(input('Digite o valor do produto: R$'))
pagamento = int(input('''FORMAS DE PAGAMENTO:
[1] À vista dinhero/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
'''))

if pagamento == 1:
    total = preco - (preco * 10 / 100)
    print('O valor final da sua compra ficará R${:.2f}!'.format(total))
elif pagamento == 2:
    total = preco - (preco * 5 / 100)
    print('O valor final da sua compra ficará R${:.2f}!'.format(total))
elif pagamento == 3:
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(preco/2))
    print('O valor final da sua compra ficará R${:.2f}!'.format(preco))
elif pagamento == 4:
    total = preco + (preco * 20 / 100)
    print('O valor final da sua compra ficará R${:.2f}!'.format(total))
else:
    print('Forma de pagamento inválida!')