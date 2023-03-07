import func

class Funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.funcionarios = []

    def adiciona_funcionarios_iniciais(self):
        for i in range(len(func.funcionarios)):
            l = Funcionarios(func.funcionarios[i], func.salarios[i])
            self.funcionarios.append(l)

    def mostra_funcionarios(self):
        for i in range(len(self.funcionarios)):
            print(f"""
Funcionário = {self.funcionarios[i].nome} - salário = {self.funcionarios[i].salario}
""")



class Cadastro():
    def __init__(self, funcionario):
        self.funcionario = funcionario
        self.login = str
        self.senha = str
        self.cadastros = []

    def adiciona_cadastro(self, classe):
        if func.verifica_funcionario(self.funcionario, )
