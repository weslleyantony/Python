s = 0
t = int(input('Quantos termos serão somados? '))
for c in range (0,t):
    n = int(input('Digite um número: '))
    s += n
print('A somatória entre os números é igual a {}.'.format(s))    
print('FIM!')    

# Alteração feita: a variável 't' simboliza QUANTOS números serão somados.
# Algoritmo mostra qual a SOMA de todos os números somados.