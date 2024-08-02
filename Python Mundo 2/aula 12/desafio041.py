from datetime import date

ano_atual = date.today().year
idade = int(input("Digite o seu ano de nascimento: "))
mirim = ano_atual - (ano_atual - 9)
infantil = ano_atual - (ano_atual - 14)
junior = ano_atual - (ano_atual - 19)
senior = ano_atual - (ano_atual - 20)

print(mirim, infantil, junior, senior)
