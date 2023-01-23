#Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado,
# calcule e imprima (saída de dados) seu perímetro e sua área.
#Observação: a saída deve estar no formato: "perímetro: x - área: y"

lado = float(input('Digite o valor correspondente ao lado de um quadrado:'))
perímetro = lado * 4
área = (lado ** 2)
print('perímetro:', perímetro, '- área:', área)