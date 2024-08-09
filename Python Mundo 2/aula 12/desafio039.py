from datetime import date

atual = date.today().year
nascimento = int(input("Digite o ano do seu nascimento: "))
idade = atual - nascimento
sexo = str(input('Qual o seu sexo?\nHomem (H)\nMulher (M) \n'))

print('-='*20)

if sexo == 'M':
    print('Pessoas do sexo feminino não precisam realizar o alistamento!')
elif sexo == 'H':
    if idade == 18:
        print('Quem nasceu no ano de {} tem {} ano(s) em {}!'.format(nascimento, idade, atual))
        print('Você deve se alistar IMEDIATAMENTE')
    elif idade < 18:
        saldo = 18 - idade
        print('Quem nasceu no ano de {} tem {} ano(s) em {}!'.format(nascimento, idade, atual))
        print("Ainda faltam {} ano(s)!".format(saldo))
        print('Seu alistamento será em {}.'.format(atual + saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Quem nasceu no ano de {} tem {} ano(s) em {}!'.format(nascimento, idade, atual))
        print('Você está atrasado {} ano(s)!'.format(saldo)) 
        print('Seu alistamento foi em {}.'.format(atual - saldo))
    elif idade < 0:
        print('Insira um ano de nascimento válido.')
        print('Ainda estamos no ano de {}!'.format(atual))
