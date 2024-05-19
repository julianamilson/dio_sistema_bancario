from Cliente import Cliente
from Cliente import Cliente
from Conta import Conta
from Historico import Historico

class Conta:

    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = '0001'
        self.cliente = cliente
        self.historico = Historico()

    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int) -> Conta:
        return cls(numero=numero, cliente=cliente)

    def saldo(self):
        return self.saldo
    
    def sacar(self, valor:float):
        if valor < self.saldo:
            self.saldo -= valor
            self.historico.adicionar_transacao()
            return True
        return False

    def depositar(self, valor:float):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao()
            return True
        return False