L = [7,2,5,4,9]
M = [5,5,6,2,1]

#verificar se a lista L maio que a lista M, componente a componente

Lmaior = True
for i in range(len(L)):
    if L[i] <= M[i]:
        LmaiorM = False
        break

C = [L[i]>M[i] for i in range(len(L))]
print(all(C))
