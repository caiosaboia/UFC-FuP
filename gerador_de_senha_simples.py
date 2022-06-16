# UFC/DEMA/FuP 2022.1 - Um gerador simples de senhas.
import random as rnd
import os.path as path


TamanhoDefault = 8 # Meu tamanho padrao de senha.
#-------------------------------------------------------

letras = "abcdefghijklmnopqrstuvwxyz"
letras += letras.upper()
numeros = "1234567890"
especiais = "!@#$%^&*()-_=+[]/\,.;:"

Caracteres = letras + numeros + especiais
Caracteres = list(Caracteres)

tamanho = input("Quantos caracteres voce deseja na senha? ")
tamanho = int(tamanho)
if tamanho < 8:
    print(f"Tamanho {tamanho} muito pequeno para a senha!")
    print(f"Utilizarei o tamanho padrao {TamanhoDefault}.")
    tamanho = TamanhoDefault

identificador = input("\nInforme um identificador para a senha (GMail, SIGAA, etc): ")

#-------------------------------------------------------
# Geracao de senhas candidatas.
#-------------------------------------------------------

while True:
    # Criamos uma senha com o tamanho apropriado
    senha = ""
    for k in range(tamanho):
        senha += rnd.choice( Caracteres )

    # Verificamos se a senha possui 1+ numero(s) e 1+ caracteres especiais
    caracteresDaSenha = set(senha)
    if len(set(numeros).intersection(caracteresDaSenha)) > 0:
        if len(set(especiais).intersection(caracteresDaSenha)) > 0:
            break

    # Se nao possui, rejeitamos a senha e tentamos de novo
    print(f"Senha rejeitada: {senha}")

# Neste ponto, uma senha valida ja foi gerada
print(f"\nSenha para <{identificador}> aceita: {senha}")

#-------------------------------------------------------
# Leitura dos dados do arquivo de senhas.
#-------------------------------------------------------

# Dicionario que ira' conter minhas senhas existentes.
MinhasSenhas = dict()

# Se o arquivo nao existe, entao nao ha senhas existentes.
# Se existe, vamos ler cada um delas.
if path.exists("meusdados.txt"):

    leitura = open("meusdados.txt", "r")

    # Lemos todas as senhas no arquivo.
    while True:
        linha = leitura.readline()
        if linha == "":
            break
        
        # Utilizamos o separador ": " para distinguir
        # entre identificador e senha
        Id_Senha = linha.split(": ")
        (umIdentificador, umaSenha) = tuple(Id_Senha)
        umaSenha = umaSenha[:-1] # Cuidado com o "\n" no final!
        
        # Guardamos o par (identificador,senha) no dicionario
        MinhasSenhas[umIdentificador] = umaSenha

    leitura.close() # Fechamos o arquivo. Importante!

# Incluimos no dicionario o novo par (identificador,senha)
# Se ja existir o identificador, a senha aassociada a ele
# sera' sobrescrita.
MinhasSenhas[identificador] = senha

#-------------------------------------------------------
# Sobrescrevemos o arquivo de senhas.
#-------------------------------------------------------
# primeiro crie um arquivo .txt como o "meusdados.txt"

escrita = open("meusdados.txt", "w") # Vai apagar tudo.

for identificador in MinhasSenhas.keys():
    senha = MinhasSenhas[identificador]
    escrita.write(f"{identificador}: {senha}\n")

escrita.close()
