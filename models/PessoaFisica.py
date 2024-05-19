from Cliente import Cliente
from datetime import datetime

class PessoaFisica(Cliente):

    def __init__(self, cpf:str, nome:str, data_nascimento:datetime, endereco:str):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento