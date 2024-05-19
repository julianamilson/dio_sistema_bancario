from Transacao import Transacao
from datetime import datetime

class Historico:

    def __init__(self):
        self._transacoes = []

    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao:Transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
        )