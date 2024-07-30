valor_imovel = float(input("Digite o valor do imóvel que será comprado: "))
valor_salario = float(input("Agora digite o valor do seu salário: "))
anos = int(input("Digite em quantos anos pretende pagar este imóvel: "))
meses = anos*12
valor_parcelas = valor_imovel/meses
valor_maximo = valor_salario*0.3

print("O seu salário é de R${:.2f} e será pago em {:.0f} meses/parcelas. O preço das parcelas ficarão em R${:.2f}".format(valor_salario, meses, valor_parcelas))

if valor_parcelas <= valor_maximo:
    print("O valor do empréstimo SERÁ aprovado pelo banco:")
else:
    print("O valor NÃO será aprovado pelo banco")
