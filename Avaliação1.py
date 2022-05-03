import random
A = ["o", "a"]
B = ["confuso", "fascinante", "substancia", "efemero", "insolito", "esplendido", "primordial", "perfeição", "onirico", "inconcebivel", "imperfeito", "categoria"]
C = ["do", "da"]
D = ["vida", "mundo", "tempo", "realidade", "alma", "intelecto", "universo", "conhecimento", "humanidade", "sociedade", "tecnologia", "verdade"]
E = ["consiste no", "consiste na"]
F = ["imperfeição", "diversidade", "contraste", "vastidão", "magia", "simplicidade", "hipocrisia", "subjetividade", "imcompreensão", "friovolidade"]

palavra1 = random.choice(A)
palavra2 = []
palavra3 = []
palavra4 = []
palavra5 = []
palavra6 = []

for x in B:
    if x[-1] == "o" or x[-1] == "e" or x[-1] == "l":
        palavra2.append(x)
    if x[-1] == "a" or x == "perfeição":
        palavra2.append(x)
print(palavra2)
