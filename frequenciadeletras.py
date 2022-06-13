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

for e in res:
    freq = res.count(e)
    print(e, freq)
