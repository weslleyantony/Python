casa = float(input("Valor da casa: R$ "))
salario = float(input("Salário do comprador: R$ "))
anos = int(input("Quantos anos de financiamento? "))
meses = anos*12
valor_parcelas = casa/meses
valor_maximo = salario*0.3

print("Para pagar um imóvel de R${:.2f} em {:.0f} anos, deverão ser pagas parcelas de R${:.2f}".format(casa, anos, valor_parcelas))

if valor_parcelas <= valor_maximo:
    print("Empréstimo ACEITO")
else:
    print("Empréstimo RECUSADO")
