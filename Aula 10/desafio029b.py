from time import sleep

vel = float(input("Qual é a velocidade atual do carro? "))
multa = 7 * (vel-80)
print("Calculando...")
sleep(2)

if vel > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h")
    print("Você deve pagar uma multa de R${:.2f}!".format(multa))
print("Tenha um bom dia! Dirija com segurança!")