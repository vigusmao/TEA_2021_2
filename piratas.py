from random import shuffle

REP = 100
N = 8000

acumulado = 0

quartos = [i for i in range(N)]

for _ in range(REP):
    
    shuffle(quartos)

    piratas_corretos = 0
    for j in range(N):
        if quartos[j] == j:
            piratas_corretos += 1

    print(piratas_corretos)


    acumulado += piratas_corretos


print("\n\nmedia = %.8f" % (acumulado / REP))    
