def endereco():
    estado = input("Informe a sigla de seu estado: ")
    cidade = input("Informe o nome da cidade: ")
    bairro = input("Informe o bairro: ")
    nro = input("Informe o numero da residência: ")
    logradouro = input("Informe o logradouro: ")

    return estado, cidade, bairro, nro, logradouro


def criar_usuario(lista_usuarios):
    cpf = input("Informe o CPF: ") # armazenar e nao pode ter 2 iguais
    if cpf in lista_usuarios:
        raise Exception("CPF is registered already!")
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
