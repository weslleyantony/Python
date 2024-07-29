dist = int(input("Escreva a distância em Km da sua viagem: "))
preco1 = dist * 0.50
preco2 = dist * 0.45

print("A sua viagem será de {} Km de distância!".format(dist))
if dist <= 200:
    print("Ela custará {:.2f} R$.".format(preco1))
else:
    print("Ela custará {:.2f} R$.".format(preco2))
print("Boa viagem!")