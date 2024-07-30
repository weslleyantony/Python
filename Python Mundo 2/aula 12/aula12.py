nome = str(input("Qual é o seu nome? "))
if nome == "Weslley":   
    print("Que nome bonito!")
elif nome == "Pedro" or nome == "Maria" or nome == "Paulo" or nome == "João":
    print("Seu nome é bem popular no Brasil, ein.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal...")
print("Seja bem vindo, {}!".format(nome))