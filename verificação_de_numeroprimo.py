L = [2, 8, 4, 6, 5]

for i in L:
   print(i)

j = 0
while j < len(L):
    print(L[j])
    j += 1

print('\n')

'''
x = 0
while x <= 0:
    num = input("Digite um número inteiro positivo:")
    x = int(num)
'''
P = []
#Verificar se ele x é primo
for x in range(1,101):
    contadora = 0
    for y in range(1,x+1):
        if x % y == 0:
            contadora += 1
            print("um divisor: {}".format(y))
    if contadora == 2:
        P.append(x)
        print("Primo!!")
    else:
        print("Não é primo")

print("Há {} números primos".format(len(P)))
print(P)
