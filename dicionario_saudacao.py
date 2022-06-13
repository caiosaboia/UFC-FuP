def mensagem(nome,sobrenome,turno,titulo):
    if turno == "manha":
        msg = "Bom dia, " + titulo + " "
    elif turno == "tarde":
        msg = "Boa tarde, " + titulo + " "
    elif turno == "noite":
        msg = "Boa noite, " + titulo + " "
    else:
        msg = "Olá, " + titulo + " "
    
    msg += nome + " " + sobrenome + "."
    return msg

saudação = mensagem("Gabryely","Saboia","tarde","Sra.")

def saudar(Dici,turno):
    print(Dici[turno])
portBR = dict()
portBR["manhã"] = "Bom dia"
portBR["tarde"] = "Boa tarde"
portBR["noite"] = "Boa noite"

ingles = dict()
ingles["manha"] = "Good Morning"
ingles["tarde"] = "Good Evening"
ingles["noite"] = "Good Night"

print(saudar(ingles,"manha"))
