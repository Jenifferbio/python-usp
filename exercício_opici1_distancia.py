#Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente,
# às coordenadas x e y de um ponto em um plano cartesiano. Os dois últimos devem corresponder, respectivamente,
# às coordenadas x e y de um outro ponto no mesmo plano.Calcule a distância entre os dois pontos. Se a distância for
# maior ou igual a 10, imprima longe na saída. Caso o contrário, quando a distância for menor que 10, imprima perto

import math
def entradas(planocartesiano, coordenada):
    return float(input('Forneça a coordenada {} para o plano cartesiano {}'.format(coordenada, planocartesiano)))

planocartesianoA = entradas('A', 'X'), entradas('A', 'Y')
planocartesianoB = entradas('B', 'X'), entradas('B', 'Y')

calculo = (planocartesianoA[0]-planocartesianoB[0])**2 + (planocartesianoA[1]-planocartesianoB[1])**2
distancia = math.sqrt(calculo)

print('longe' if distancia >= 10 else 'perto')
