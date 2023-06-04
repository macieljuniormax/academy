class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Motocicleta(Veiculo):
    def __init__(self, tipo, chassi, marca, modelo, ano, cilindradas):
        super().__init__(tipo, chassi, marca, modelo, ano)
        self.cilindradas = cilindradas


v = Veiculo("carro", "23232323232323", "Ferrari", "F112",  2017)
print(vars(v))

m = Motocicleta("motocicleta", "3232323232323", "Honda", "CG", "2008", 150)
print(vars(m))