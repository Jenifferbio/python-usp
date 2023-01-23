import math
a = float(input('Informe o valor de a'))
b = float(input('Informe o valor de b'))
c = float(input('Informe o valor de c'))
delta = b ** 2 - 4 * a * c

if (delta == 0):
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print('A única raiz é', raiz1)

#Não é possível fazer raiz quadrada quando o delta é negativo, por isso tenho que verificar o caso antes com um if dentro do else
#Importante observar a indentação que subordina blocos if e else dentre de um bloco maior else
else:
    if delta < 0:
        print('Esta equação não possui raízes reais')
    else:
        # Esse comando se repete, pensar em algo melhor
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print('A primeira raiz é', raiz1)
        print('A segunda raiz é', raiz2)
