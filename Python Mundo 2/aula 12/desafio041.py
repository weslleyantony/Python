from datetime import date

ano = int(input("Digite o ano do seu nascimento: "))
idade = date.today().year - ano

if idade <= 9:
    print("Sua idade é de {} anos. A sua categoria correta é MIRIM".format(idade))
elif idade <= 14:
    print("Sua idade é de {} anos. A sua categoria correta é INFANTIL".format(idade))
elif idade <=19:
    print("Sua idade é de {} anos. A sua categoria correta é JUNIOR".format(idade))
elif idade <=25:
    print("Sua idade é de {} anos. A sua categoria correta é SÊNIOR".format(idade))
else:
    print("Sua idade é de {} anos. A sua categoria correta é MASTER".format(idade))