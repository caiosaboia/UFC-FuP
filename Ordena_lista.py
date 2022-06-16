import random as rnd

L = []
for i in range(7):
    L.append(rnd.randint(1,20))
print(L)

estarordenada = 0
for j in range(len(L)-1):
    if L[j] <= L[j+1]:
        estarordenada = False
        break

if estarordenada == True:
    print("Lista ordenada")
else:
    print("não está ordenada")
