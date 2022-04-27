import random

L = []
for indice in range(20):
    L.append(random.randint(1,100))
print(L)

soma = 0
for x in L:
    if x % 2 == 0:
        soma = soma + x
print("A soma dos pares é: ", soma)

