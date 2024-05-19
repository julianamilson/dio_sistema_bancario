from Conta import Conta
from abc import ABC

class Transacao(ABC):

    def __init__(self):
        pass

    @classmethod
    def registrar(self, conta:Conta):
        pass
