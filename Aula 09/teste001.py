n = str(input("Digite o seu nome completo: "))
nome = n.split()
pnome = nome[0].title()
unome = nome[len(nome)-1].title()

print("O seu primeiro nome é '{}'".format(pnome))
print("O seu último nome é '{}'".format(unome))
print("É um prazer te conhecer {} {}!".format(pnome,unome))