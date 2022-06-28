# UFC/DEMA, FuP 2022.1
import datetime

LOG_ATIVADO = True # Se o programa vai registrar os erros em arquivo

# Este sera' o arquivo de log (registros de eventos do programa)
arqLog = open("log.txt", "a")

# Registra uma mensagem junto com o tempo e o nome do usuario
def logar(usu, msg):
    if LOG_ATIVADO == True:
        arqLog.write(f"[{datetime.datetime.now()}] U: {usu} {msg}\n")

# Ler nome do usuario e registrar no arquivo de log
nome = input("Digite seu nome: ")
logar(nome, "Logou-se.")

while True: # laco infinito

    # Tente executar o que esta' dentro da clausula <try>
    try:
        idade = input("Digite sua idade: ")
        # Se houver erro na conversao para int, o fluxo do programa ira'
        # para a clausula <except>
        idade = int(float(idade))
        
        # Se chegou ate aqui e' porque nao houve nenhum erro; portanto,
        # podemos sair do laco <while>
        break

    # Esta clausula ira' tratar um erro do tipo <ValueError>, se acontecer
    except ValueError:
        print("Digite um valor numerico, pfvr.")
        logar(nome, "Entrou com idade invalida.")

# Aqui, geramos um erro proprio nosso, caso seja uma situacao da qual nao
# queremos nos recuperar, mas que desejamos causar o fim do programa.
assert idade != 0, "Erro grave: idade nao pode ser zero!"

# Registrar fim do programa
logar(nome, "Fim de sessao.")

# Fechar o arquivo de log -- importante. Desligue tambem o estabilizador do lab.
arqLog.close()
