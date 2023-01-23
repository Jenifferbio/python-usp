#Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito
# com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

nsalvo = n = int(input('Digite um numero inteiro'))

anterior = n % 10
n = n // 10;
niguais = False;
pos = 0

while n > 0 and not niguais:
    atual = n % 10
    if atual == anterior:
        niguais = True
    else:
        pos += 1
    anterior = atual
    n = n // 10

if niguais:
    print('sim')
else:
    print('não')
