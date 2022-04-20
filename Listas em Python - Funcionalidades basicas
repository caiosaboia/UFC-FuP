# UFC/DEMA, FuP 2022.1
# Listas em Python - Funcionalidades bÃ¡sicas

# Duas formas de criar uma lista inicialmente vazia
L = list()
L = []
print(L)

# Acrescentando elementos um por um
# InserÃ§Ã£o com append sempre acontece no final da lista
L.append(5)
L.append("abcd")
L.append(19.3)
print(L) # A ordem de inserÃ§Ã£o Ã© preservada

# Verificar pertinÃªncia de elementos na lista
print(5 in L)
print(6 in L)
print(6 not in L)

# Redefinir a lista implica perder seu conteÃºdo
L = []
print(L)

# Podemos criar lista nÃ£o-vazia
L = [19.3, 5, "abcd"]
print(L)

# Acessamos os elementos de uma lista como fazemos com uma string
print(L[0])
print(L[-1])

# Podemos modificar os elementos de uma lista
L[2] = L[2] + "efgh"
print(L)
L[2] = "abc"
print(L)

# Uma lista pode conter listas, que podem conter listas, etc
L.append([6, 5, 4])
print(L)

# O valor 6 nÃ£o estÃ¡ na lista, porque Ã© [6, 5, 4] quem estÃ¡ em L
print(6 in L)

print( L[2:4] ) # Imprime os elementos de Ã­ndice 2 e 3.

# Outros operadores de fatiamento tambÃ©m funcionam:
print( L[3:] )
print( L[0::2] )
print( L[::-1] )

# Obter tamanho de L
print( len(L) )

print( L.pop() ) # Remove e "devolve" o Ãºltimo elemento
print(L)

print( L.pop(1) ) # Remove e "devolve" o elemento de Ã­ndice 1
print(L)

# Acrescentando vÃ¡rios elementos simultaneamente na lista
# Corresponde a uma sequÃªncia de operaÃ§Ãµes do tipo append
L.extend( [2, 5, 2, 2, 7, 1, 2, 8] )
print(L)

# TambÃ©m podemos usar o operador "+", de soma
# Note que nÃ£o estamos alterando L, mas criando temporariamente
# uma nova lista que contÃ©m o conteÃºdo de L e de [10,20,30].
print( L + [10,20,30] )

# Remove o primeiro elemento igual a 2
L.remove(2) # NÃƒO remove todos os elementos iguais a 2
print(L)

del L[1] # Remove o elemento armazenado na posiÃ§Ã£o de indice 1
print(L)

# Obter a posiÃ§Ã£o do valor 5 na lista
print( L.index(5) )
# CUIDADO: sÃ³ use .index() se souber que o valor pertence a L
if 17 in L:
    print( L.index(17) )

# Inserir elemento em uma posiÃ§Ã£o arbitrÃ¡ria da lista
L.insert(3, 999)
print(L)

L.insert(0, 111)
print(L)

# CUIDADO: nÃ£o insira em posiÃ§Ã£o inexistente:
if len(L) >= 10:
    L.insert(10, 444)
print(L)

# Contando o nÃºmero de vezes que elemento aparece na lista
print( f"{L.count(2)} elementos iguais a 2" )

# Percorrendo os elementos de uma lista
for elemento in L:
    print("   ", elemento)

# Outra forma de percorrer os elementos de uma lista
# range(K) nos dÃ¡ uma "espÃ©cie de lista" contendo 0, 1, ..., K-1.
# Veremos depois que tipo de objeto o range realmente nos devolve.
for indice in range(len(L)):
    print(f"L[{indice}] = ", L[indice])

# Realizando alguma modificaÃ§Ã£o sobre cada elemento
for i in range(len(L)):
    L[i] = L[i] + L[i]
print(L)

A = [1,2,3]
B = [4,5,6]

# Lembre-se de que "in" possui precedÃªncia baixa
if 5 in A+B:
    print("Pertence.")
else:
    print("NÃ£o pertence.")

if 5 in A+B and 8 not in B:
    print("OK.")
else:
    print("NÃ£o OK.")

# Criar uma cÃ³pia ordenada da lista
M = sorted(L)
print(M)

# Ordenar a prÃ³pria lista L
L.sort()
print(L)

# ComparaÃ§Ã£o de listas
print(L == M)



