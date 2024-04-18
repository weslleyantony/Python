print("-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20)
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Os segmentos acima \033[1;32;40mPODEM\033[m formar um triângulo!")
else:
    print("Os segmentos acima \033[1;31;40mNÃO PODEM\033[m formar um triângulo!")