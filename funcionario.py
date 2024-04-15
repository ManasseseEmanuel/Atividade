class Funcionario:
    def __init__(self,id,nome,salario):
        self.id = id
        self.nome = nome
        self.salario = salario

    def aumentar_salario (self, percentual):
        self.salario = self.salario + (self.salario*percentual)

class Gerente(Funcionario):
    def __init__(self,id,nome,salario,departamento):
        super().__init__(id,nome,salario)
        self.departamento = departamento

    def promover_funcionario (self,funcionario):
        self.salario = self.salario + (self.salario*0,10)

class FuncionarioRegular(Funcionario):
    def __init__(self,id,nome,salario):
        super().__init__(id,nome,salario)

    def calcular_folha_pagamento(lista_funcionarios):
        total_folha = 0
        for funcionario in lista_funcionarios:
            total_folha += funcionario.salario
        return total_folha
    
fun01 = FuncionarioRegular('Carla', 1, 1500.00 )
fun02 = FuncionarioRegular('Laura', 2, 10000.00)
gen1 = Gerente('Helena',  3, 20000.00, 'RH' )
gen2 = Gerente('Manuela', 4, 15000.00, 'Segurança')

lista_funcionario = [fun01, fun02, gen1, gen2]
total_folha_pag = FuncionarioRegular.calcular_folha_pagamento(lista_funcionario)
print(total_folha_pag)
