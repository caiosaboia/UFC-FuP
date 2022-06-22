import random as rnd
import itertools as it

#---------------------------------------------------------------
# Funcao que retorna True de a tuple de tuplas <q> formar um
# quadrado latino, e Retorna False, caso contrario.
def verifica_se_latino(q):
    e = True
    ordem = len(q)
    for coluna in range(ordem):
        S = {q[linha][coluna] for linha in range(ordem)}
        if len(S) != ordem:
            e = False
            break
    return e

# Fucao que imprime de forma legivel um quadrado latino.
def imprimir(q):
    ordem = len(q)

    print("")
    for linha in range(ordem):
        for coluna in range(ordem):
            print(f"{q[linha][coluna]:3d}", end="")
        print("")

#---------------------------------------------------------------
N = int(input('Qual o tamanho do seu quadrado latino: ')) # Ordem dos quadrados desejados

# Construir uma lista com as permutacoes dos numeros de 1 a N
Ps = list(it.permutations(range(1,N+1)))

contadorQL = 0 # Contador de quadrados latinos encontrados

# Faz produto cartesiano de N permutacoes no conjunto Ps
for q in it.product(Ps, repeat=N):
    # Se formar um quadrado latino, imprimir e contar
    if verifica_se_latino(q):
        imprimir(q) # Comente esta linha para rodar + rapido
        contadorQL += 1
        # De 100 em 100 quadrados, imprime o contador, para
        # termos ideia de como a enumeracao esta progredindo
        if contadorQL % 100 == 0:
            print(contadorQL)

print(f"\nTotal de quadrados latinos: {contadorQL}")
