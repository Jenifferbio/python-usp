#Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

n = int(input('Digite o valor de n'))
resultado = 1
count = 1
while count <= n:
    resultado *= count
    count += 1
print(resultado)