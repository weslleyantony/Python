vel = float(input("Digite a velocidade do seu carro: "))
multa = (vel - 80) * 7

if vel > 80:
    print("Você foi multado! Estava a {}Km/h.".format(vel))
    print("A multa custará {:.2f} R$.".format(multa))
else:
    print("Estava na velocidade correta, pode seguir em frente!")