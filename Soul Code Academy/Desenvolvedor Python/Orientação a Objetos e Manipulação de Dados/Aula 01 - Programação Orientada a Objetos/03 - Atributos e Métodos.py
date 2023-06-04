class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def get_salario(self):
        print("Meu salário é: R$", self.salario)

    def get_bonificacao(self):
        return self.salario * 0.15

    def set_salario(self, salario):
        self.salario = self


maciel = Funcionario("Maciel", "11606214624", 5000)
maciel.get_salario()
print(maciel.get_bonificacao())

