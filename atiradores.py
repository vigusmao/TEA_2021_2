

### Problema dos atiradores do clube


### A: acendeu luz verde ([A]certou o tiro)
### B: trata-se do atirador [B]om

### Pr{A|B} = 80%


### Pr{A|B'} = 30%



#### Pr{B} =  ??????


### Pergunta: dada uma sequença de "luzes", qual a probabilidade de ser o atirador bom?

### Pr{B|A} = Pr{B&A}        /       Pr{A}
###         = Pr{B}.Pr{A|B}  /       Pr{B}.Pr{A|B} + Pr{B'}.Pr{A|B'}       (Bayes)


from random import random

Pr_A_dado_B = 0.8
Pr_A_dado_nao_B = 0.2

Pr_B = 0.5 #### chute inicial!! (probabilidade aprioristica)


for i in range(100):
    #luz = input("Acertou?")
    #acertou = luz in ["s","S","sim","y"]
    acertou = random() < Pr_A_dado_B
        

    if acertou:
        Pr_B = (Pr_B * Pr_A_dado_B) /   (Pr_B * Pr_A_dado_B + (1-Pr_B) * Pr_A_dado_nao_B)

    else:
        Pr_B = (Pr_B * (1 - Pr_A_dado_B)) /   \
               (Pr_B * (1 - Pr_A_dado_B) + (1-Pr_B) * (1 - Pr_A_dado_nao_B))

    print("verde" if acertou else "vermelho", " --> ", Pr_B)
    


