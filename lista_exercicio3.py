numero = input("Escolha um número: ")
numero = int(numero)

if (numero % 10) == 0:
    print("divisivel 10")
    if (numero % 2) == 0:
        print("divisivel 2")
    if (numero % 5) == 0:
        print("divisivel 5")
else:
    print("nao é divisivel por porra nenhuma") 
    



  