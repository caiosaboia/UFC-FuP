import random

L = []
for indice in range(20):
    L.append(random.randint(1,100))
print(L)

M = []
for x in L:
    if x > 50:
        M.append(x)
print("Esses são os elementos maiores que 50:\n", M)
