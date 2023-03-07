funcionarios = ['Pedro' , 'Ana'   , 'Carlos', 'Maria Clara', 'João Antonio']
salarios     = [ 3470.00,  2200.00,  3970.34,  7450.23     ,  5677.33 ]

def verifica_funcionario(funcionario, lista):
    if funcionario not in lista.funcionarios:
        input("Funcionário não existe. ENTER para continuar.")
        return False
    return True
