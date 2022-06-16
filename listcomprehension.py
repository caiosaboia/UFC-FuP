import random as rnd
import sys
'''
L = [rnd.randint(1,50) for i in range(10)] #list comprehension
print(L)
print("\n")

A = {rnd.randint(1,50) for i in range(10)} #set comprehension
print(A)

print(sys.getsizeof(L))
print(sys.getsizeof(A))

G = (rnd.randint(1,50) for i in range(10)) #generator

print(sys.getsizeof(G))
'''
L = [i**2 for i in range(10)]
G = (i**2 for i in range(10))

#for x in G:
#   print(x)
#print("\n")

def gerade5a1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def gera01():
    v = 0
    while True:
        yield v
        if v == 0:
            v = 1
        else:
            v = 0

k = 1
for x in gera01():
    print(x)
    k += 1
    if k == 10:
        break 
print("\n")

def fib():
    yield 1
    yield 1
    a = 1
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c

''' #Aqui é função de fibonate funcionando com o laço
k = 1
for x in fib():
    print(x)
    k += 1
    if k == 11:
        break 
'''

it = iter(fib())

# Posso gerar um range, como:

for _ in range(10):
    print(next(it))

print( next(it)) # posso repetir esse comando quantas vezes eu quiser.

it2 = iter(fib())

print(next(it2))
print(next(it))
print(next(it2))

print('\n')

K = (x*2 for x in range(10))
for i in K:
    print(i)

# Vejamos que se vc colocar isso parar roda ele, a lista 
#
# for i in K:
#    print("Linha ajuda")
#    print(i)

print('\n'*2)

def minha(s):
    return s[:-1]

N = ["gato", "cachorro", "lesma"]

#M = map(str.upper, N) #o map pertece ao type str(string)
M = map(minha, N)

for x in M:
    print(x)

'''
#Vejamos um outro exemplo bem util que podemos aplicar:

def minha(s):
    return s**2

N = [5, 6, 7]

M = map(minha, M)

for x in M:
    print(x)
'''


