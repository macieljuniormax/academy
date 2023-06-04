class Animal:
    def __init__(self, especie, cor, habitat):
        self.especie = especie
        self.cor = cor
        self.habitat = habitat


class Inseto(Animal):
    def __init__(self, especie, cor, habitat, asas, venenoso):
        super().__init__(especie, cor, habitat)
        self.asas = asas
        self.venenoso = venenoso


aranha = Inseto("aranha", "marrom", "floresta", 0, True)
mosca = Inseto("mosca", "amarela", "bosta", 4, False)

print(vars(aranha))
print(vars(mosca))
