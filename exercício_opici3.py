#Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
n = int(input('Digite um número inteiro'))
print(n)
d = (n//10) % 10
print('O digito das dezenas é', d)