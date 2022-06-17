import random

L = [] # L = list()
#inseridos em L 20 inteniros de 1 a 100 (Original)
for _indice in range(5):#teste
    L.append(random.randint(1,10))#teste

print(L)

#Aqui esta a questao de fato: (so o caio msm pra saber a ordem dessas coisas msm pqp)
soma = 0
for x in L:
    if x % 2 == 0:
        soma = soma + x

print("A soma dos pares é", soma)
