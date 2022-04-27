import random 

L = []

for indice in range(20):
    L.append(random.randint(1,100))
print(L)

M = []

for x in L:
    if x % 2 == 0:
        M.append(x)
print(M)