def fatorial (n):
    fat = 1 #elemento neutro da multiplicação
    while (n > 1): #enquanto essa expressão for verdadeira, eu vou repetir essa função booleana
        fat = fat * n #O valor novo do fatorial fat será o valor antigo de fatorial vezes n
        n = n - 1 #O valor novo do n, vai ser o valor antigo do n -1
    return fat

def numero_binomial(n, k):
    return fatorial(n)/ (fatorial(k) * fatorial(n-k))

def testa_fatorial():
    if fatorial(1) == 1:
        print('funciona para 1')
    else:
        print('não funciona para 1')
    if fatorial(2) == 2:
        print('funciona para 2')
    else:
        print('não funciona para 2')
    if fatorial(0) == 1:
        print('funciona para 0')
    else:
        print('não funciona para 0')
    if fatorial(5) == 120:
        print('funciona para 5')
    else:
        print('não funciona para 5')



