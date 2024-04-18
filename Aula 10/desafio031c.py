distancia = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}Km.".format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("O valor da sua viagem será de {:.2f}R$!".format(preço))