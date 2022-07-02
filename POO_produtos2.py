import datetime

class Produto:
    
    def __init__(self, anome, apreco, asecao, aestoque):
        self.__nome = anome
        self.__preco = apreco
        self.__secao = asecao
        self.__estoque = aestoque
        self.__log = None
    
    def log(self, destino=None):
        self.__log = destino
    
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_secao(self):
        return self.__secao
    def get_estoque(self):
        return self.__estoque

    def set_nome(self, novonome):
        if self.__log != None:
            self.__log(f"Modificando nome: {self.__nome} --> {novonome}.")
        self.__nome = novonome

    def set_preco(self, novopreco):
        if self.__log != None:
            self.__log(f"Modificando preco de <{self.__nome}>: {self.__preco} --> {novopreco}.")
        self.__preco = novopreco
   
    def set_secao(self, novasecao):
        self.__secao = novasecao
    
    def set_estoque(self, novoestoque):
        if self.__log != None:
            self.__log(f"Modificando estoque de <{self.__nome}>: {self.__estoque} --> {novoestoque}.")
        self.__estoque = novoestoque

    def __str__(self):
        return f"Produto: ({self.get_nome()}, preco R${self.__preco})"

def logar_em_arquivo(mensagem):
    
    arq = open("registros.txt", "a")

    agora = datetime.datetime.now()
    texto = agora.strftime('%d/%m/%Y %H:%M:%S')
    arq.write(f"[{texto}] {mensagem}\n")

    arq.close()

#-----------------------------------------------------------------------------------------------------------
if __name__ == "__main__":

    p = Produto("batata", 4.52, "hortifruti", 500)
    p.log(print)
    #p.log(logar_em_arquivo)
    
    print(p)

    p.set_preco(7.29)

    print(p)
