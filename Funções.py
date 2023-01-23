#Aqui temos a sintaxe para utilização de funções no Python

'''def NOME (PARÂMETROS):
    COMANDOS'''

#Definindo uma função
#A palavra reservada def inicia a definição de uma função. Ela deve ser seguida do nome da função e da
# lista de parâmetros formais entre parênteses. Os comandos que formam o corpo da função
# começam na linha seguinte e devem ser indentados.

'''def is_nucleotide_valid(nucleotide):
    nucleotide_list = ['A', 'C', 'T', 'G']
    nucleotide = nucleotide.upper()

    if nucleotide in nucleotide_list:
        print(f"{nucleotide} é um nucleotídeo válido")
    else:
        print(f"{nucleotide} NÃO é um nucleotídeo válido")
letra = 'A'
is_nucleotide_valid(letra)

is_nucleotide_valid('K')

response = is_nucleotide_valid('T')
print(response)'''

# Função para somar números
'''def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

# Chamando a função e passando parâmetros
addNum(20, 5)'''

#Comando return
'''def is_nucleotide_valid(nucleotide):
  nucleotide = nucleotide.upper()
  nucleotide_list = ['A', 'C', 'T', 'G']
  if nucleotide in nucleotide_list:
    return True
  else:
    return False

def soma(x, y):
      result = x + y
      return result

a = int(input("Primeiro numero: "))
b = int(input("Segundo numero : "))
res = soma(a, b)
print("Soma: ", res)'''

#Função lambda
#Cria pequenas funções anônimas

'''def mult_2(n):
  return n*2
lambda_mult = lambda n: n*2
numeros = [8,5,9,1]

for n in numeros:
  print(mult_2(n))'''

'''preço = 1000
def calcular_imposto (preço):
  return preço*0.3

print(calcular_imposto(preço))

calcular_imposto2 = lambda x: x*0.3

print(calcular_imposto2(preço))'''

'''Docstrings seriam as famosas aspas triplas, 
que são úteis para explicar para quê serve cada linha do código'''

'''#Função sem parâmetro
def nome_do_seu_cachorro ():
    return 'Alegre'''

'''#Função que retorna a soma dos comprimentos de 3 palavras ou frases:
def total_Caracteres (x, y, z):
    return len(x)+len(y)+len(z)

#"Desenvolva uma função que devolva um número lido, maior que zero"
def leitura():
    x = int(input("Digite um valor: "))
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x

#ou

def leitura():
    x = -1
    while x <= 0:
        x = int(input("Digite um valor: "))
    return x'''



