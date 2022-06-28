# UFC/DEMA/FuP 2022.1
import itertools as it

L = [2, 8, 5, 17, 9, 3]
palavra = "Satélite"

# Tudo que fazemos a seguir pode ser feito tambem utilizando-se
# a variavel <palavra> no lugar de <L>.

# A funcao iter() cria um iterador para um objeto iteravel. Este
# iterador e' uma maneira de nos referenciarmos ao primeiro elemento
# do objeto iteravel em questao. Este objeto iteravel pode ser uma
# lista, uma tupla, um dicionario, um gerador, etc.

# A funcao next() avanca o iterador, que passa a apontar para o
# proximo elemento do objeto iteravel. Alem de avancar o iterador,
# ela tambem retorna o item do objeto iteravel para o qual estava
# apontando. Se o objeto iteravel fosse um gerador, isto significa
# que o elemento era gerado e o gerador ficaria pronto para gerar o
# elemento seguinte.

# Caso o gerador tenha sido esgotado, ou todos os elementos do objeto
# iteravel tenham sido visitados pelo iterador, o uso de next() gera
# um erro/excecao do tipo <StopIteration>, que pode ser capturado para
# evitar o termino do programa. Assim, podemos percorrer qualquer
# objeto iteravel sem utilizar diretamente um laco <for>.

i = iter(L)  # Cria um iterador para <L>
i2 = iter(L) # Cria um iterador para <L>
next(i2)     # Avanca o iterador <i2>, que passa a apontar para
             # o segundo elemento de <L>

# A funcao itertools.tee() recebe um objeto iteravel e um inteiro e
# retorna uma tupla de iteradores, do tamanho do inteiro fornecido.
# Alternativamente, poderiamos substituir as tres linhas de codigo
# acima por:
# (i,i2) = it.tee(L); next(i2)

# Aqui, vamos consumir os dois iteradores, usando a funcao next().
while True:
    try:
        print(next(i), next(i2))
    except StopIteration:
        break

# Uma maneira alternativa de fazer isso seria com um <for>:
for c in range( len(L) - 1 ):
    print( L[c], L[c+1] )

# Uma construcao mais elaborada, com 4 iteradores pode ser vista abaixo.
# Neste exemplo, estamos criando uma tupla com 4 iteradores e fazendo
# cada um deles apontar para um dos primeiros elementos: o primeiro
# iterador aponta para o primeiro elemento de <L>, o segundo aponta para
# o segundo elemento, e assim por diante.
t = it.tee(L, 4)
for a in range(len(t)):
    for _ in range(a):
        next(t[a])

# Como um exemplo, vamos imprimir os elementos de acordo com uma ordem 
# bem particular: elementos de indice 0, 1 e 3; depois, os elementos
# 1, 2 e 4, etc. Sempre pulando o terceiro elemento em cada sequencia.
for y in zip(t[0], t[1], t[3]):
    print(y)

