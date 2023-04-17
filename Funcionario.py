class Funcionario:
    def __init__(self, nome, idade, data_admissao, setor, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.data_admissao = data_admissao
        self.setor = setor
        self.salario = salario
        self.cargo = cargo
        self.status = "Ativo"