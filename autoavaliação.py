# L é uma lista com n-quaisquer valores
# M é a nova lista que a funçao vai gerar.
# Aqui é a resolução da primeira questao.
L = [1,-2, 3, -5, 4]
print("Aqui jás a saída da primeira questão: \n", L)
def q1(L):
    M = []
    for x in L:
        if x > 0:
            M.append(x)
    return M
print(q1(L), "\n")


#P é uma lista com numeros aleatorios a partir de outra funçao(que usamos em sala por sinal)
import random as rnd
def listarandom(tam):
    return [rnd.randint(1,100) for i in range(tam)]
P = listarandom(10)
print("Aqui a jás a saída da segunda questão:\n",P)

def q2(P):
    M = []
    for i in P:
        if i % 2 != 0 and i % 3 != 0:
            M.append(i)
    return M

print(q2(P))
        
         








    

