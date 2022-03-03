import sys
from random import randint

def subset_sum(lista):
    sys.setrecursionlimit(2 * len(lista) + 1000)
    memo = {}
    alvo = sum(lista) / 2
    return solve(lista, 0, alvo, memo)

def solve(l, start, w, memo):

    # estah no memo?
    result_from_memo = memo.get((start, w))
    if result_from_memo is not None:
        return result_from_memo

    # nao estava no memo, trata-se da primeira vez
    # em que recebemos este exato subproblema --
    # vamos resolve-lo normalmente, via recursao    

    v1 = l[start]  # valor do primeiro elemento considerado

    # base da recursao
    if start == len(l) - 1:
        result = v1 if v1 <= w else 0        
    
    else:
        solucao_com_o_primeiro = \
            v1 + \
            solve(l, start + 1, w - v1, memo) if v1 <= w else 0 
    
        solucao_sem_o_primeiro = \
            solve(l, start + 1, w, memo)

        result = max(solucao_com_o_primeiro, \
                     solucao_sem_o_primeiro)

    memo[(start, w)] = result

    return result 





#lista = input("Digite a lista: ")

lista = [randint(1, 100) for _ in range(200)]
print subset_sum(lista)






 
