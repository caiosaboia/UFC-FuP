numero = int(input("Escolha um número: "))

if numero % 10 == 0:
    print("È divisivel por 2\nÉ divisivel por 5\nÉ divisivel por 10")
else:
    print("Não é divisivel por 10")

    if numero % 2 == 0:
        print("Divisivel por 2")
    else:
        print("Não é divisivel por 2")
    if numero % 5 == 0:
        print("É divisivel por 5")
    else:
        print("Não é divisivel por 5")
if numero % 35 == 0:
    print("É divisivel por 7\nÉ divisivel por 35")
else:
    print("Não é divisivel por 35")
    if numero % 7 == 0:
        print("É divisivel por 7")
    else:
        print("Não é divisivel por 7")
    



  
