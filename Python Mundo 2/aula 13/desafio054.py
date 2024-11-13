from datetime import date
ano = date.today().year
totmai = 0
totmen = 0

for c in range (1,8):
    idade = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    dif = ano - idade
    if dif >= 18:
        totmai += 1
    elif dif < 18:
        totmen += 1
print('Temos {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade'.format(totmai,totmen))

