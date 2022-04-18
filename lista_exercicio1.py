numero = int(input("Digite qualquer número com mais de 2 algarismos: ").lstrip())
print(f"Você digitou: {numero}")
string = int(str(numero)[::-1])

print(f'O numero invertido e sem o zeros é {string}')

if numero > string:
    print("Seu numero é maior que seu espelho")
elif numero == string:
    print("Seu numero é igual ao seu espelho")
else:
    print("Seu numero é menor que seu espelho")
