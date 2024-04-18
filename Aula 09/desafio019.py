from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

alunos = [n1, n2, n3, n4]
escolhido = choice(alunos)

print('Na sala temos os alunos {}, {}, {} e {}, porém o escolhido foi o {}'.format(n1, n2, n3, n4, escolhido))