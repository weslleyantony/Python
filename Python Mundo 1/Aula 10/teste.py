escolha = str(input("Esolha um lado: Direita ou Esquerda? ")).strip().upper()

esquerda = """carro.siga()
carro.direita()
carro.siga()
carro.direita()
carro.esquerda()
carro.siga()
carro.direita()
carro siga()"""

direita = """carro.siga()
carro.esquerda()
carro.siga()
carro.esquerda()
carro.siga()"""

if escolha == 'DIREITA':
    print(direita)
else:
    print(esquerda)
    
print("FIM!")