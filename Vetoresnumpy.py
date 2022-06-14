import numpy as np

# Criacao de um vetor unidimensional:
vet = np.array((1, 2, 3, 4, 5))
print("vet =", vet)

# Vetor com duas dimensoes:
vetor = np.array((1, 2, 3, 4, 5), ndmin=2)
print("vetor =", vetor)
print("vetor[0] =", vetor[0])
print("vetor[0][2] =", vetor[0][2])
print("vetor[0,2] =", vetor[0,2])

print("\n")

# Soma de vetores (componente a componente):
v = np.array((1, 2, 3, 4, 5))
print("v =", v)
w = np.array([0, 2, 0, 1, 2])
print("w =", w)

print("v + w:", v+w)

print("Soma de listas:", [1, 2, 3, 4, 5] + [0, 2, 0, 1, 2])

print("2*v =", 2*v)

print("\n")
