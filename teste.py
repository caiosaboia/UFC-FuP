idade = input("qual é sua idade? ")
idade = int(idade)

if idade == 16 or idade == 17:
    print("pode votar, mas é facultativo.")
elif idade > 70:
    print("pode votar, mas também é facultativo.")

if idade >= 18 and idade <= 70:
    print("Voto obrigatório")

if idade < 16:
    print("Não pode votar.")
    