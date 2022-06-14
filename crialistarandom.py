import random as rnd

def criarlista(tam):
    return [rnd.randint(1,20) for i in range(tam)]

L = criarlista(10)
print(L)
