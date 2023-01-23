#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
# como parâmetro e devolve o maior número primo menor ou igual ao número passado à função

#o valor é passado como parâmetro para a função
def maior_primo(n):
#o bloco for irá iterar - quantas vezes for necessário - sobre o range(n, 1, -1)
    for c in range(n, 1, -1):
#Em cada uma dessas iterações o bloco if perguntará à função primo() se o valor de c é de fato um número primo
        if éprimo(c):
#Então, a função éprimo() calculará os divisores de c e se o número de divisores for igual à 2, enviará o valor True
#como resposta ao bloco if da função maior_primo().Caso contrário, enviará False como resposta.
            return c

def éprimo(m):
#i = inicializar e 1 porque é o elemento neutro da multiplicação
    i = 1
    cont = 0
#enquanto i for menor ou igual à variável m, que significa múltiplo
    while i <= m:
#se o resto da divisão de m por i for 0, se for, m é múltiplo de i, logo não é primo.
#por isso, deve ser somado 1 à variável cont
        if m % i == 0:
            cont += 1
        i += 1
        if cont > 2:
            return False
    return True


num = int(input('Digite um número inteiro maior que "1"'))

print(maior_primo(num))