#UFC/DEMA, 2022.1
import itertools as it

# Retorna True se x for impar, False se for par
def impar(x):
    return x % 2 != 0

L = [6, 3, 8, 0, 54, 7, 2]

# Retorna um gerador que aplica a funcao <impar> a
# todos os elementos de L
I = filter(impar, L)

print(list(I))
print(list(I))

# Alguns exemplos de funcoes lambda
parteInteira = lambda x: x if x>=0 else 0
print( parteInteira(-94) )

somaModulos = lambda x, y: abs(x) + abs(y)
print( somaModulos(-6, 17) )

# Um gerador criado a partir de uma funcao lambda
I = filter(lambda a: True if a%2 == 1 else 0, L)
print(list(I))

#--------------------------------------------------

print("\nContando a partir de dado valor (com passo):")
for x in it.count(5, 7):
    print(x)
    if x > 50:
        break


print("\nRepeticao ciclica:")
for (i,x) in enumerate(it.cycle([0,1])):
    print(x)
    if i > 7:
        break


print("\nSalva os elementos do iteravel, mesmo que gerador:")
I = filter(lambda a: True if a%2 == 1 else 0, L)
for (i,x) in enumerate(it.cycle(I)):
    print(x)
    if i > 7:
        break


print("\nRepetir algo para sempre, ou um determinado numero de vezes:")
for x in it.repeat(45,6):
    print(x)
    
#---------------------------------

print("\nSoma cumulativa:")
Ac = it.accumulate(L)
for x in Ac:
    print(x)


print("\nConcatenacao de iteraveis:")
Y = it.chain(L,'ABCD')
for y in Y:
    print(y)


print("\nRetornar todos os elementos a partir do primeiro False:")
Y = it.dropwhile(lambda x: x != 0, L)
for y in Y:
    print(y)


print("\nPermutacoes:")
Y = it.permutations("ABCD", r=2)
for y in Y:
    print(y)


print("\nCombinacoes:")
Y = it.combinations("ABCD", r=2)
for y in Y:
    print(y)


print("\nCombinacoes com reposicao:")
Y = it.combinations_with_replacement("ABCD", r=2)
for y in Y:
    print(y)


print("\nProduto cartesiano:")
Y = it.product("ABCD", [1,2])
for y in Y:
    print(y)


print("\nCompressao/Selecao (similar a filter):")
Y = it.compress("ABCD", [1,0,0,1])
for y in Y:
    print(y)

#--------------------------------------------------
# Problema da Mochila (ver definicao na Wikipedia)
# 
# Utiliza um gerador (itertools.product) para
# enumerar todas as combinacoes de escolhas. 
# Verifica se cada combinacao e' uma solucao
# valida (viavel) do problema.

def total(precos, sol):
    itens = it.compress(precos,sol)
    return sum(itens)

def viavel(pesos, sol, capacidade):
    return sum(it.compress(pesos,sol)) <= capacidade

v = [10, 5, 15, 7, 6, 18, 3]
p = [2, 3, 5, 7, 1, 4, 1]
B = 15
n = len(v)
valor_otimo = 0
sol_otima = []

for candidata in it.product([0,1], repeat=n):
    if viavel(p, candidata, B):
        z = total(v, candidata)
        if sol_otima == [] or z > valor_otimo:
            valor_otimo = z
            sol_otima = candidata

print(valor_otimo)
print(sol_otima)
