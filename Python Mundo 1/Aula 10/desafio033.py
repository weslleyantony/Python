valor1 = int(input("Primeiro Valor: "))
valor2 = int(input("Segundo Valor: "))
valor3 = int(input("Terceiro Valor: "))

#VERIFICANDO QUEM É O MENOR VALOR
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
#VERIFICANDO QUEM É O MAIOR VALOR
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor2 and valor3 > valor1:
    maior = valor3

print("O MENOR valor digitado foi {}.".format(menor))
print("O MAIOR valor digitado foi {}.".format(maior))