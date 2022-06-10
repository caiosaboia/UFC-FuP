import random as rnd

def criarLista(nels):
    return [ rnd.randint(1,100) for i in range(nels) ]

def linhas(A, nLin, nCol):

    for i in range(nLin):
        linha = []
        for j in range(nCol):
            linha.append(A[i*nCol + j])
        yield linha

def colunas(A, nLin, nCol):

    for j in range(nCol):
        coluna = []
        for i in range(nLin):
            coluna.append(A[i*nCol + j])
        yield coluna

def matriz(L, nLin, nCol):
    A = []
    for l in linhas(L, nLin, nCol):
        A.append(l)
    return A

def imprimirMatriz(M):
    nLin = len(M)
    nCol = len(M[0])
    
    for i in range(nLin):
        for j in range(nCol):
            print("{:3}".format(M[i][j]), end=" ")
        print("")
    print("")

Dados = criarLista(12)
print( Dados )
print("")

for l in linhas(Dados, 3, 4):
    print(l)
print("")

for c in colunas(Dados, 3, 4):
    print(c)
print("")

print( matriz(Dados, 3, 4) )
print("")

print( matriz(Dados, 2, 6) )
print("")

print( matriz(Dados, 6, 2) )
print("")

A = matriz(Dados, 3, 4)
imprimirMatriz(A)
