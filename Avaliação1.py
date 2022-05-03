import random
A = ["O", "A"]
B = ["confuso", "fascinante", "efêmero", "insólito", "esplendido", "primordial", "onírico", "inconcebivel", "imperfeito", "perfeição", "categoria", "substância"]
C = ["do", "da"]
D = ["mundo", "tempo", "intelécto", "universo", "conhecimento", "sociedade", "tecnologia", "verdade", "vida", "realidade", "alma",  "humanidade"]
E = ["consiste no", "consiste na"]
F = ["contraste", "vastidão", "magia", "simplicidade", "hipocrisia", "subjetividade", "incompreensão", "frivolidade", "imperfeição", "diversidade"]
for x in range(0,5):
    p1 = A[random.randint(0,1)]
    p3 = C[random.randint(0,1)]
    p5 = E[random.randint(0,1)]
    if p1 == "O":
        p2 = B[random.randint(0,8)]
    else:
        p2 = B[random.randint(9,11)]
    if p3 == "do":
        p4 = D[random.randint(0,4)]
    else:
        p4 = D[random.randint(5,11)]
    if p5 == "consiste na":
        p6 = F[random.randint(1,9)]
    else:
        p6 = "constraste"
    print('{} {} {} {} {} {}'.format(p1, p2, p3, p4, p5, p6))
