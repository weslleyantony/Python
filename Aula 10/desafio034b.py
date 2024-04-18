salario = float(input("Qual é o salário do funcionário? "))

if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print("O seu salário sairá de R${:.2f} e passará a ser R${:.2f}.".format(salario, aumento))
else:
    aumento = salario + (salario * 10 / 100)
    print("O seu salário sairá de R${:.2f} e passará a ser R${:.2f}.".format(salario, aumento))