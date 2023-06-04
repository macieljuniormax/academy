class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca, cor):
        self.__marca = marca
        self.__cor = cor

    @property
    def marca(self):
        return self.__marca

    @property
    def cor(self):
        return self.cor

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @staticmethod
    def escrever():
        print("A caneta está escrevendo 🖋️")


escritor = Escritor("Maciel")
caneta = Caneta("BIC", "Azul")

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
