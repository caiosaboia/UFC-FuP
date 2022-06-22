# UFC/DEMA/FuP 2022.1
# Execicio sugerido: vizinhos mais proximos.
# Assista ao video correspondente para detalhes.

import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import math

Dados = []

rnd.seed(8) # Fixe uma semente, se assim desejar

for i in range(40):
    x = rnd.random()*10
    y = rnd.random()*10
    tipo = rnd.randint(0,1)
    
    ponto = np.array([x, y, tipo])
    Dados.append(ponto)
    
    if tipo == 0:
        plt.plot(x, y, 'b*')
    else:
        plt.plot(x, y, 'r*')

x = float(input("Digite o valor da abscissa (x): "))
y = float(input("Digite o valor da ordenada (y): "))
k = int(input("Quantos vizinhos voce deseja utilizar? "))

plt.plot(x, y, 'go')


#----------------------------------------------------------------

def distanciaEuclidiana(P1, P2):
    dist = 0
    for i in range(len(P1)):
        dist += (P1[i] - P2[i])**2
    return math.sqrt(dist)

def distanciaManhattan(P1, P2):
    dist = 0
    for i in range(len(P1)):
        dist += abs(P1[i] - P2[i])
    return dist

# Funcao generica que calcula a previsao, de acordo com os vizinhos mais proximos.
# A nocao de vizinho dependende diretamente da <metrica>, que corresponde aa nocao
# de distancia a ser utilizada. Diferentes metricas podem corresponder a
# diferentes conjuntos de vizinho e, consequentemente, a diferentes previsoes.
def VizinhosMaisProximos(metrica):
    # Calcular distancias, de acordo com a metrica fornecida
    Distancias = []
    for ponto in Dados:
        P = [ponto[0],ponto[1]]
        d = metrica(P, [x,y])
        Distancias.append(d)

    # Determinar vizinhos mais proximos
    maiorDist = max(Distancias)
    ContTipo0 = 0
    ContTipo1 = 0
    for j in range(k):
        mp = np.argmin(Distancias)
        print(f"{j+1}-esimo vizinho: {Dados[mp]} (dist: {Distancias[mp]:5.3f})")
        Distancias[mp] = 1+maiorDist
        if Dados[mp][2] == 0:
            ContTipo0 += 1
        else:
            ContTipo1 += 1
        plt.plot([x, Dados[mp][0]], [y, Dados[mp][1]], 'g-')

    # Imprimir previsao
    print(f"Previsao: tipo {0 if ContTipo0 > ContTipo1 else 1}")

# Invocando o algoritmo de vizinhos mais proximos com a nocao de
# distancia quarteirao ou Manhattan.
VizinhosMaisProximos(distanciaManhattan)

#----------------------------------------------------------------
# Deixe este comando no final do programa, ja que
# ele paralisa a execucao do mesmo:
plt.show()
