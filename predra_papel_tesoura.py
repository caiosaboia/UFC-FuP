print ("Helo World")
print("+-----------------------+")
print("| Preda, papel, tesoura |")
print("+-----------------------+")

jogadaU = input("Qual sua jogada? ")

import random

escolha = random.randint(1,3)

if escolha == 1:
    jogadaC = "Tesoura"
elif escolha == 2:
    jogadaC = "Preda"
else:
    jogadaC = "Papel"

print("O computador jogou {}".format(jogadaC))

if jogadaC == "Papel":

    if jogadaU == "Tesoura":
        print("Usuário(a) vence!")
    elif jogadaU == "Preda":
        print("Computador vence!")
    else:
        print("Empate!")

elif jogadaC == "Tesoura":

    if jogadaU == "Tesoura":
        print("Empate!")
    elif jogadaU == "Preda":
        print("Usuário(a) vence!")
    else:
        print("Computador vence!")

else: # Aqui computador jogo Preda

    if jogadaU == "Tesoura":
        print("Computador vence!")
    elif jogadaU == "Preda":
        print("Empate!")
    else:
        print("Usuário(a) vence!")
