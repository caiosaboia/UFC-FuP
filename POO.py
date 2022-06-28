# UFC/DEMA/FuP 2022.1
# Programacao orientada a objetos (POO) - Parte 1
import random
'''
Uma classe e' um tipo de objeto em que Python que e' composto de dados e
de um conjunto de operacoes ou comportamentos/funcionalidades. Ate o
momento, ja utilizamos varias classes, tais como str, list, dict, etc.
A classe list, por exemplo, contem os dados da propria lista, assim como
uma serie de funcoes, que correspondem a comportamentos ou funcionalidades.
Estas funcoes sao chamadas de metodos. Quando utilizamos list.sort(), os
dados da lista sao ordenados, o que significa que chamar aquela funcao tem
efeito sobre o conteudo da lista, assim como acontece com as funcoes
list.remove(), list.append(), etc.

Alem das classes que ja existem no Python, podemos criar nossas proprias
classes. A motivacao principal para criar classes e' que cada classe pode
corresponder a alguma entidade real do dominio da aplicacao que estamos
desenvolvendo. Os dados de uma classe ficam organizados dentro de uma mesma
variavel (esta variavel e' chamada de um objeto daquela classe) e estes
dados ficam acessiveis apenas por meio das funcoes que existem na classe (o
conjunto destas funcoes e' chamado de "interface" da classe).'''

# Exemplo: classe <pessoa>
class pessoa:

    # Construtor da classe - funcao especial que e' chamada quando criamos
    # um objeto desta classe. O argumento <self> e' obrigatorio aqui e nos
    # metodos, exceto em alguns casos especiais.
    def __init__(self, nome, idade, numeros):
        self._nome = nome
        assert idade >= 0, "Nao posso criar pessoa com idade < 0"
        self._idade = idade
        self._numerosSorte = numeros

    # __str__() e' uma funcao que e' chamada quando tentamos conventer um
    # objeto da classe para um valor do tipo <str>, seja quando convertemos
    # explicitamente, utilizando str(objeto) ou quando chamamos <print>.
    # Sem este metodo, o Python nao sabe imprimir objetos desta classe.
    def __str__(self):
        s = f"O-<-< ({self._nome}, {self._idade})"
        return s

    # O metodos __repr__() e' semelhante ao __str__(), mas normalmente fornece
    # uma representacao do objeto que e' permite recria-lo dentro do cÃ³digo.
    # Neste exemplo, o __repr__() devolve uma string que, se colada dentro do
    # codigo-fonte, recria um objeto da classe <pessoa> identico ao objeto atual.
    def __repr__(self):
        s = f'pessoa("{self._nome}", {self._idade}, {self._numerosSorte})'
        return s

    # Metodo utilizado para ordenacao de colecoes de objetos da classe <pessoa>.
    # <lt> corresponde a "less than" e retorn True se o objeto atual e' "menor que"
    # o objeto <outra>. Esta funcao e' chamada quando fazemos algo assim: pes1<pes2,
    # onde <pes1> e <pes2> sao objetos da classe <pesssoa>. Sem esse metodo, nao e'
    # possivel, por exemplo, ordenar uma lista de objetos da classe <pesssoa>.
    def __lt__(self, outra):
        return self._nome < outra._nome

    # Metodo do tipo "get", que devolvem os dados do objeto atual.
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_numeros(self):
        return self._numerosSorte
    
    # Este metodo retorna um dos numeros da sorte da pessoa. A escolha e'
    # aleatoria, com base na lista <self._numerosSorte>.
    def palpite(self):
        return random.choice( self._numerosSorte )

    # Aumenta a idade do objeto atual.
    def faz_aniversario(self):
        self._idade += 1

    # Metodo do tipo "set", que altera os dados do objeto atual.
    # Neste caso, podemos controlar o tipo de alteracao permitido. Aqui, nao
    # permitimos reduzir a idade da pessoa.
    def set_idade(self, novaidade):
        if novaidade > self._idade:
            self._idade = novaidade

    # Metodos podem apenas fornecer respostas baseadas nos dados internos do objeto.
    # Aqui, responde-se True/False, de acordo com a idade da pessoa.
    def maior_de_idade(self):
        if self._idade >= 18:
            return True
        else:
            return False

pes1 = pessoa("Joao", 19, [5, 17, 33])
pes2 = pessoa("Andrea", 15, [1, 7])
pes3 = pessoa("Zumira", 21, [4, 5, 6])

L = [pes1, pes2, pes3]
print(L)

# Ordena a lista de acordo com o metodo __lt__():
L.sort()
print(L)

# Ordena a lista de acordo com o nome, em ordem decrescente:
L.sort(key = lambda x: x.get_nome(), reverse=True)
print(L)
