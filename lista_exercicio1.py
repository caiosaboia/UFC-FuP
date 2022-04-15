numero = str(input("Digite qualquer número com mais de 2 algarismos: "))
print("Você digitou: {}".format(numero))
string = numero[::-1]
print("O espelho do seu número é: {}".format(string))

if numero < string:
    print("Este número é menor que seu espelho.")
elif numero == string:
    print("Este número é igual ao seu espelho")
else:
    print("Este número é maior que seu espelho.")
