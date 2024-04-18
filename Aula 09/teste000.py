n = str(input("Digite o seu nome completo: ")).strip()
nome = n.split()

print("O seu primero nome é '{}'".format(nome[0].title()))
print("O seu último nome é '{}'".format(nome[len(nome)-1].title()))
print("É um prazer em te conhecer {} {}!".format(nome[0].title(), nome[len(nome)-1].title()))