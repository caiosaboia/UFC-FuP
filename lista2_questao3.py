import random

L = []

for indice in range(20):
    L.append(random.randint(1,100))
print(L)

for x in L:
    if x > 50:
        print("Lá vem o homem-macaco!")
                