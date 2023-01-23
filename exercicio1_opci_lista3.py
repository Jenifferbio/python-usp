#Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo. Se o número for primo,
# imprima "primo". Caso contrário, imprima "não primo".

n = int(input('Digite um numero inteiro'))
if (n // 2) == 0:
    print('primo')
else:
    print('não primo')