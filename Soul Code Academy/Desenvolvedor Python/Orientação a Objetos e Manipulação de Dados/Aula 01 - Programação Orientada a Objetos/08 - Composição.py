class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        self.__enderecos = []

    @property
    def nome(self):
        return self.__nome

    @property
    def enderecos(self):
        return self.__enderecos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def inserir_endereco(self, cidade):
        self.__enderecos.append(Endereco(cidade))

    def listar_enderecos(self):
        for endereco in self.__enderecos:
            print(endereco.cidade)


class Endereco:
    def __init__(self, cidade):
        self.__cidade = cidade

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade


cliente_1 = Cliente("Maciel")
cliente_1.inserir_endereco("Brasília")
print(cliente_1.nome)
cliente_1.listar_enderecos()

del cliente_1
print(cliente_1.nome)
cliente_1.listar_enderecos()