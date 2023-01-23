import math

a = int(input('informe o valor de a'))
b = int(input('informe o valor de b'))
c = int(input('informe o valor de c'))

d = (b ** 2) - (4 * a * c)

if d == 0:
        r1 = (-b + math.sqrt(d))/(2*a)
        print('a raiz desta equação é', r1)
else:
    if d > 0:
            r1 = (-b + math.sqrt(d))/(2*a)
            r2 = (-b - math.sqrt(d))/(2*a)
            if r1 < r2:
                print('as raízes desta equação são', r1, 'e', r2)
            else:
                print('as raízes desta equação são', r2, 'e', r1)
    else:
        print('esta equação não possui raízes reais')


