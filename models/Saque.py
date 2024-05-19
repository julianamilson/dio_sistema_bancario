from Conta import Conta
from Transacao import Transacao

class Saque(Transacao):

    def __init__(self, valor:float):
        self.valor = valor

    def valor(self):
        return self.valor

    def registrar(self, conta:Conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)