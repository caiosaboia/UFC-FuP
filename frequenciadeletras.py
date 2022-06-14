def SomaProdutos(L):
    soma = 0; prod = 1
    for x in L:
        soma += x
        prod *= x
    return (soma,prod)


def obtemLetras(texto):
    L = []
    for x in texto:
        L.append(x)
    return L
res = obtemLetras("minha terra tem palmeiras")
print(res)

#Creio que essa de baixo seja nao recursiva

for e in res:
    freq = res.count(e)
    print(e, freq)
    
def obtemFrequencias(texto):
    D = dict()

    for letra in texto:
        valor = D.get(letra)
        if valor == None:
            D[letra] = 1
        else:
            D[letra] = valor +1

    return D

print(obtemFrequencias("minha terra tem palmeiras"))
