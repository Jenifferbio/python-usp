'''print('Digite uma sequência de valores terminada por zero')
soma = 0

valor = 1
while valor != 0:
    valor = int(input('Digite um valor a ser somado:'))
    soma = soma + valor
print('A soma dos valores digitados é', soma)'''

'''tamanho = int(input('Digite o tamanho da sequência de números:'))
produto = 1
#i começa em zero e vai contando de 1 em 1
i = 0

#quando o i for menor que o tamanho, ae então vai repetir
while i < tamanho:
    valor = int(input('Digite um valor a ser multiplicado:'))
    produto = produto * valor
    i = i + 1

print('O produto dos dois valores digitados é:', produto)'''

#programa para calcular a soma dos dígitos de um número inteiro grande
n = int(input('Digite um número inteiro com muitos dígitos:'))
soma = 0

while (n > 0):
    resto = n % 10 #guarda o último numeral de n
    n = (n - resto)//10 #remove o último dígito de n
    soma = soma + resto #soma
print('A soma dos digitos digitados é', soma)

