from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
parametro = ano_atual - ano_nascimento
atraso = (ano_atual - ano_nascimento) - 18
diferenca_menor = ano_nascimento - (ano_atual - 18)
diferenca_maior = ano_atual - atraso

if parametro <= 17:
    print("Você ainda irá se alistar daqui {} ano(s)!".format(diferenca_menor))
elif parametro == 18:
    print("Está na hora! Você deve se alistar este ano!")
else:
    print("O tempo já passou! Deveria ter se alistado há {} ano(s) atrás, em {}!".format(atraso, diferenca_maior)) 
