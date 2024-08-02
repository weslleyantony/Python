nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))
media = (nota1 + nota2)/2

print("A sua média foi igual a {}".format(media))

if media < 5.0:
    print("Você está REPROVADO!")
elif media <= 6.9:
    print("Você está na RECUPERAÇÃO!")
else: 
    print("Você está APROVADO! Parabéns!!!")