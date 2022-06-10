from random import shuffle, randint
from itertools import permutations

def quadradoslatino(N):
    auxiliar = []
    for _ in range(1,N+1):
        auxiliar.append(_)
    shuffle(auxiliar)
    quadrofeito = []
    quadrofeito.append(auxiliar)

    permutacao = permutations(auxiliar)
    for _ in permutacao:
        _ = list(_)
        if analise(quadrofeito, _) == True:
            quadrofeito.append(_)
    
    for _ in quadrofeito:
        print(_)

def analise(p,q):
    for w in range(len(p)):    
        for z in range(len(p[0])):
            if p[w][z] == q[z]:
                return False
    return True

Tamanho = int(input('Qual o tamanho do seu quadro? '))
quadradoslatino(Tamanho)
