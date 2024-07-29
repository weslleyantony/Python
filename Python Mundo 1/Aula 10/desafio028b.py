from random import randint
from time import sleep

print("-=-"*25)
print("Estou pensando em um número entra 0 e 5...")
print("-=-"*25)
numero = int(input("Qual número eu pensei? "))
res = randint(0,5)
print("Processando...")
sleep(2)

if numero > 5 or numero < 0:
    print("\033[1;33;40mNúmero Inválido! Digite um número entre 0 e 5.\033[m")
elif numero == res:
    print("Parabéns, este era o número \033[1;32;40mcorreto\033[m")
else:
    print("Você \033[1;31;40merrou\033[m! O número correto era \033[1;32;40m{}\033[m".format(res))