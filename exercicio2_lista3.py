#Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo.

inteiros = int(input('Digite o valor de n'))
i = 0
impar = 1
while i < inteiros:
    print(impar)
    i = i + 1
    impar = impar + 2


