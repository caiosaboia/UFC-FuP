class Pessoa:
    
    def __init__(self, anome):
        self.__nome = anome
    
    def get_nome(self):
        return self.__nome

    def __str__(self):
        return f"Pessoa {self.get_nome()}"

class Estudante(Pessoa):

    def __init__(self, anome, amatricula):
        self.__matricula = amatricula
        super().__init__(anome)
    
    def get_matricula(self):
        return self.__matricula

    def __str__(self):
        return f"Estudante {self.get_nome()} ({self.get_matricula()})"

class Intercambista(Estudante):
    
    def __init__(self, anome, amatricula, apais):
        self.__pais = apais
        super().__init__(anome, amatricula)

    def get_pais(self):
        return self.__pais
    
    def __str__(self):
        return f"Intercambista {self.get_nome()} ({self.get_pais()})"

# Se este e' o arquivo principal, e nao um arquivo incluido via <import>
if __name__ == "__main__":

    p1 = Pessoa("Rafael Pereira")
    print(p1)

    # Duas formas equivalentes de chamar um metodo:
    print(p1.get_nome())
    print(Pessoa.get_nome(p1))


    a1 = Estudante("Andre Andrade", 6489)

    print(a1)
    print(a1.get_nome())

    e1 = Intercambista("Jose Gonzalez", 9922, "Chile")
    print(e1)

# Se este arquivo foi incluido via <import>
else:
    print("Estou sendo incluido noutro programa. Socorro!")
