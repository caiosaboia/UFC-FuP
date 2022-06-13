#Função recursiva de fibonate
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fib(n-1) + fib(n-2)
    
#Função nao-recursiva de fibonate
def fib_naorecursiva(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        ultimo = 1
        penultimo = 1
        atual = ultimo + penultimo 

        for i in range(n-3):
            penultimo = ultimo 
            ultimo = atual
            atual = ultimo + penultimo

        return atual

for i in range(1,20):
    print(fib_naorecursiva(i), end=" ")
print("\n")
print(fib_naorecursiva(20))
