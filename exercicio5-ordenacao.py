#Receba 3 números inteiros na entrada e imprima crescente se eles forem dados em ordem crescente.
# Caso contrário, imprima não está em ordem crescente

n1 = int(input('Informe o primeiro números inteiro'))
n2 = int(input('Informe o segundo números inteiro'))
n3 = int(input('Informe o terceiro números inteiro'))
if (n3>n2>n1):
    print('crescente')
else:
    print('não está em ordem crescente')