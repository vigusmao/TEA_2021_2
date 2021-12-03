from random import random

REP = 100000


acumulado = 0

for _ in range(REP):
    cont = 1 
    while random() >= 0.4:
        cont += 1

    acumulado += cont


print("media = %.3f" % (acumulado / REP))
    

