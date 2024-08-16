nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

print("Com as notas tiradas, de {} e {}, a sua média foi igual a {}".format(nota1, nota2, media))

if media < 5.0:
    print("Você está REPROVADO!")
elif media < 7.0:
    print("Você está na RECUPERAÇÃO!")
else: 
    print("Você está APROVADO! Parabéns!!!")