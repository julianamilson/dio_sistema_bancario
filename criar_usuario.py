from utils import posicao_cpf

def endereco():
    estado = input("Informe a sigla de seu estado: ")
    cidade = input("Informe o nome da cidade: ")
    bairro = input("Informe o bairro: ")
    nro = input("Informe o numero da residência: ")
    logradouro = input("Informe o logradouro: ")

    return estado, cidade, bairro, nro, logradouro


def criar_usuario(lista_usuarios):
    cpf = int(input("Informe o CPF: ")) # armazenar e nao pode ter 2 iguais
    if posicao_cpf(lista_usuarios, cpf) != -42:
        print("CPF is registered already!")
        return None
    else:
        nome = input("Informe o nome: ")
        nascimento = input("Informe a data de nascimento: ")
        estado, cidade, bairro, nro, logradouro = endereco()
        usuario = {
            'nome': nome,
            'nascimento': nascimento,
            'endereco': f'{logradouro}, {nro} - {bairro} - {cidade}/{estado}', 
            'contas_correntes' : []
        }
        return cpf, usuario
