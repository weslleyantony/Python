peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura**2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}: \033[7;30mAbaixo do Peso\033[m'.format(imc))
    print('O seu IMC é igual a {:.2f}'.format(imc))
elif imc <=25:
    print('Seu IMC é de {:.2f}: \033[0;42mPeso Ideal\033[m'.format(imc))
    print('O seu IMC é igual a {:.2f}'.format(imc))
elif imc <=30:
    print('Seu IMC é de {:.2f}: \033[0;43mSobrepeso\033[m'.format(imc))
    print('O seu IMC é igual a {:.2f}'.format(imc))
elif imc <=40:
    print('Seu IMC é de {:.2f}: \033[0;41mObesidade\033[m'.format(imc))
    print('O seu IMC é igual a {:.2f}'.format(imc))
else: 
    print('Seu IMC é de {:.2f}: \033[0;45mObesidade Mórbida\033[m'.format(imc))
    print('O seu IMC é igual a {:.2f}'.format(imc))