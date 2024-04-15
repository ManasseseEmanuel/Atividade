class Cliente: 
    def _init_(self,  nome, cpf, contas):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

class Conta: 
    def _init_(self, num_conta,saldo,transacao):
        self.num_conta = num_conta
        self.saldo = saldo
        self.transacao = []

    def depositar (self,dinheiro):
        self.saldo = self.saldo + dinheiro
        self.transacao.append(("Deposito: ",dinheiro))
    
    def sacar (self,dinheiro):
        if self.saldo > dinheiro:
            self.saldo = self.saldo - dinheiro
            self.transacao.append (("Saque: ", dinheiro))
        else:
            print ("Seu saldo é insuficiente")

    def registrar_transacao (self, tipo, valor):
        self.transacao.append((tipo ,":", valor))

    def extrato (self):
        print("Extrato da conta: ", self.num_conta)
        print ("Transação: ")
        for tipo,valor in self.transacao:
            print(tipo, ":" ,valor )
        print ("Saldo atual : ",self.saldo)

class conta_C(Conta): 
    def _init_(self, num_conta, saldo, taxa_juros,tipo_conta = "Corrente"):
        super()._init_(num_conta, saldo)
        self.tipo_conta = tipo_conta

class conta_p(Conta): 
    def _init_(self, num_conta, saldo, taxa_juros, tipo_conta = "Poupança"):
        super()._init_(num_conta, saldo, )
        self.tipo_conta = tipo_conta
        self.taxa_juros = taxa_juros

From funcao import Cliente
From funcao import Conta
From funcao import conta_C
From funcao import conta_p

cliente1 = Cliente("João", "123.456.789-00")
cliente2 = Cliente("Maria", "987.654.321-00")

conta_corrente1 = ContaCorrente("001", tipo_conta='Corrente')
conta_poupanca1 = ContaPoupanca("101", taxa_juros=0.02)

cliente1.abrir_conta(conta_corrente1)
cliente1.abrir_conta(conta_poupanca1)

conta_corrente2 = ContaCorrente("002", tipo_conta='Corrente')
conta_poupanca2 = ContaPoupanca("102", taxa_juros=0.03)

cliente2.abrir_conta(conta_corrente2)
cliente2.abrir_conta(conta_poupanca2)

conta_corrente1.depositar(1000)
conta_corrente1.sacar(500)
conta_corrente1.registrar_transacao('Transferência Recebida', 200)

conta_poupanca1.depositar(5000)
conta_poupanca1.calcular_juros()

conta_corrente2.depositar(1500)
conta_corrente2.sacar(200)
conta_corrente2.registrar_transacao('Pagamento de Conta', 100)

conta_poupanca2.depositar(3000)
conta_poupanca2.calcular_juros()

conta_corrente1.extrato()
print("--------------------")
conta_poupanca1.extrato()
print("--------------------")
conta_corrente2.extrato()
print("--------------------")
conta_poupanca2.extrato()
print("--------------------")
