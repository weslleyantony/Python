from time import sleep

dist = float(input("Qual é a distância da sua viagem? "))
#print("Calculando...")
# sleep(2)
print("Você está prestes a começar uma viagem de {:.2f}Km.".format(dist))

if dist <= 200:
    preco = 0.50
else:
    preco = dist * 0.45
print("A sua viagem irá custar {:.2f}R$.".format(preco))
print("Tenha uma ótima viagem")