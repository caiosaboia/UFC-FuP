def citacao(nome, meio, sobrenome):
    cit = sobrenome.upper()
    cit += ", " + nome[0].upper() + "."
    cit += meio[0].upper() + "."
    return cit

pessoa = dict()
pessoa["nome"] = "Caio"
pessoa["meio"] = "Rubem"
pessoa["sobrenome"] = "Saboia"

print(citacao(**pessoa))
