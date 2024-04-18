import random

print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
numero = int(input("Em que número eu pensei? "))
escolhido = random.randint(0,5)

if numero == escolhido:
    print("SIMMM! Parabéns, o número era {}.".format(escolhido))
elif numero > 5:
    print("Número inválido! Digite um número entre 0 e 5.")
else:
    print("Que pena, você errou. O número era {}.".format(escolhido))