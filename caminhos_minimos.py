import numpy as np
import itertools as it

def descricao(C): #funçao para inserir as coordenadas em direções
    texto = ""
    for p in C:
        if p[0] == 0:
            if p[1] == 1:
                texto += "D"
            else:
                texto += "E"
        elif p[0] == 1:
            texto += "B"
        else:
            texto += "C"
    
    return texto

inicio = np.array([4,3]) #Aqui temos [linha,coluna]
destino = np.array([0,1]) #Outra [linha, coluna]

buraco = [(1,3),(2,2)]

#np.array([1,0]) anda pra baixo
#np.array([0,1]) anda pra esquerda
#np.array([-1,0]) anda pra cima
#np.array([0,-1]) anda direita 

passos = [np.array([1,0]),np.array([0,1]),np.array([-1,0]),np.array([0,-1])]

for k in range(1,10):
    chegou = False
    for caminho in it.product(passos, repeat=k):
        atual = np.array(inicio)
        
        for passo in caminho:
            atual += passo
            if atual[0] < 0 or atual[0] > 4 or atual[1] < 0 or atual[1] > 4:
                break
            if tuple(atual) in buraco:
                break


        if all(atual == destino):
            print(descricao(caminho))
            print("Chegou!")
            chegou = True
            break
    
    if chegou == True:
        break
    
print("Fim.")