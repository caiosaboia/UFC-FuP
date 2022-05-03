import random
A = ["O", "A"]
B = ["confuso", "fascinante", "efemero", "insolito", "esplendido", "primordial", "onirico", "inconcebivel", "imperfeito", "perfeição", "categoria", "substancia"]
C = ["do", "da"]
D = ["mundo", "tempo", "intelecto", "universo", "conhecimento", "sociedade", "tecnologia", "verdade", "vida", "realidade", "alma",  "humanidade"]
E = ["consiste no", "consiste na"]
F = ["contraste", "vastidão", "magia", "simplicidade", "hipocrisia", "subjetividade", "imcompreensão", "friovolidade", "imperfeição", "diversidade",]
for x in range(0,5):
    palavra1 = A[random.randint(0,1)]
    palavra3 = C[random.randint(0,1)]
    palavra5 = E[random.randint(0,1)]
    if palavra1 == "O":
        palavra2 = B[random.randint(0,8)]
    else:
        palavra2 = B[random.randint(9,11)]

    if palavra3 == "do":
        palavra4 = D[random.randint(0,4)]
    else:
        palavra4 = D[random.randint(5,11)]

    if palavra5 == "consiste na":
        palavra6 = F[random.randint(1,9)]
    else:
        palavra6 = "constraste"
    print('{} {} {} {} {} {}'.format(palavra1, palavra2, palavra3, palavra4, palavra5, palavra6))
