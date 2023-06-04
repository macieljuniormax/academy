class Veiculo:
    def __init__(self, tipo, chassi, marca, modelo, ano):
        self.tipo = tipo
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Aviao:
    def __init__(self, tipo, motor, linha_area, modelo, ano):
        self.tipo = tipo
        self.motor = motor
        self.linha_aerea = linha_area
        self.modelo = modelo
        self.ano = ano


carro = Veiculo("carro", "94737348343943", "Marca X", "X001", "2012")
print(vars(carro))

aviao = Aviao("carga", "quadrimotor", "Soul Code AirLines", "AirBus 380", "2010")
print(vars(aviao))
