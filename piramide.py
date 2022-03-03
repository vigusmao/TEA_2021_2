####                   0                       0,0
####                 0   1                1,0           1,1
####               0   1   2          2,0     2,1    2,1*  2,2*
####             0   1   2   3     3,0    3,1 3,1* 3,2        
####           0   1   2   3   4  4,0 4,1
#                
#                                 tamanho da arvore =
#                                 #nos_internos + #folhas
#                             <= #nos_internos  + 2.#nos_internos
#                             <= 3.#nos_internos
#                             <= 3.#subproblemas_distintos
#                              = 3. n*n   = O(n^2)
#
#
#  RECEITA: complexidade da PD = complexidade_de_cada_chamada *
#                                numero_de_filhos_por_chamada *
#                                numero_de_subproblemas_distintos
#
#     neste caso, O(1) . O(1) . O(n^2) = O(n^2)
#
# 
import sys
from random import randint
from time import time

somas_encontradas = None
memo = None


def min_sum(piramide):
    global somas_encontradas
    global memo

    somas_encontradas = []
    memo = {}  # hash map
    sys.setrecursionlimit(2*len(piramide))

#    start = time()
#    print("backtracking...")
#    solve_backtracking(piramide, 0, 0, 0)
#    print min(somas_encontradas)
#    print("tempo = %.3f" % (time() - start))

    start = time()
    print("pd...")
    print solve_pd(piramide, 0, 0)
    print("tempo = %.3f" % (time() - start))


# retorna a menor soma de uma pirade com topo (linha, coluna)
def solve_pd(piramide, linha, coluna):

    id_subproblema = (linha, coluna)
    result_from_memo = memo.get(id_subproblema)
    if result_from_memo is not None:
        return result_from_memo
   
    if linha == len(piramide) - 1:
        return piramide[linha][coluna]

    custo_otimo_pela_esquerda = \
        solve_pd(piramide, linha+1, coluna)
    
    custo_otimo_pela_direita = \
        solve_pd(piramide, linha+1, coluna+1)
    
    custo_otimo = piramide[linha][coluna] + \
        min(custo_otimo_pela_esquerda, custo_otimo_pela_direita) 

    memo[id_subproblema] = custo_otimo

    return custo_otimo	


def solve_backtracking(piramide, linha, coluna, soma_parcial):
    # estou indo para a posicao [linha, coluna] da piramide
    soma_parcial += piramide[linha][coluna]

    # ja estou no ultimo nivel da piramide?
    if linha == len(piramide) - 1:
        # tenho uma solucao viavel na mao, vou guarda-la!
        somas_encontradas.append(soma_parcial)
        return 

    # para cada candidato (a proximo passo) possivel...
    
    # candidato 1: desco pela esquerda
    solve_backtracking(piramide, linha+1, coluna, soma_parcial) 

    # candidato 2: desco pela direita
    solve_backtracking(piramide, linha+1, coluna+1, soma_parcial)


# main

while True:
    n = int(input("altura da piramide: "))
    if n < 1:
        break

    piramide = []
    for l in range(n):
        linha = []
        for coluna in range(l+1):
            linha.append(randint(0, 9))
        piramide.append(linha)

#    print(piramide)

    min_sum(piramide)

    print("\n\n")






