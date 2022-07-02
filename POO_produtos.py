import datetime

class Produto:

    instancias = 0

    def __init__(self, anome, apreco, asecao, aestoque):
        self.__nome = anome
        self.__preco = apreco
        self.__secao = asecao
        self.__estoque = aestoque
        self.__log = None
        self.__class__.instancias += 1
   
    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    def get_secao(self):
        return self.__secao
    def get_estoque(self):
        return self.__estoque

    def __str__(self):
        return f"Produto: ({self.get_nome()}, preco R${self.__preco})"

    @classmethod
    def get_instancias(cls):
        return cls.instancias

    @staticmethod
    def teste():
        p = Produto("batata", 4.52, "hortifruti", 500)
        print(p)
        print("Instancias:", Produto.get_instancias())

if __name__ == "__main__":

    Produto.teste()
    
    q = Produto("quiabo", 2.99, "hortifruti", 150)
    print(q)
    print("Instancias:", Produto.get_instancias())
