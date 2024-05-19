from Transacao import Transacao
from Conta import Conta

class Deposito(Transacao):

    def __init__(self, valor:float):
        self.valor = valor
    
    def valor(self):
        return self.valor

    def registrar(self, conta:Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)