salario = float(input("Digite o seu salário: "))
aumento10 = salario + (salario*10/100)
aumento15 = salario + (salario*15/100)

if salario <= 1250:
    print("Reajuste de 15%! O seu salário passará de {:.2f}R$ para {:.2f}R$!".format(salario, aumento15))
else:
    print("Reajuste de 10%! O seu salário passará de {:.2f}R$ para {:.2f}R$".format(salario, aumento10))