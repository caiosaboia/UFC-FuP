import random

K = []
for indice in range(20):
    K.append(random.randint(1,100))
print(K)

M = []
for _ in K:
    if _ > 90:
        print("Lá vem o homem-macaco!")
    else:
        print("RECEBA!!!")
