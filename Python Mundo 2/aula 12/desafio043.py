peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura*altura)

if imc < 18.5:
    print('Seu IMC é de {:.2f}: Abaixo do Peso'.format(imc))
elif imc <=25:
    print('Seu IMC é de {:.2f}: Peso Ideal'.format(imc))
elif imc <=30:
    print('Seu IMC é de {:.2f}: Sobrepeso'.format(imc))
elif imc <=40:
    print('Seu IMC é de {:.2f}: Obesidade'.format(imc))
else: 
    print('Seu IMC é de {:.2f}: Obesidade Mórbida'.format(imc))