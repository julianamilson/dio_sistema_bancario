def criar_conta_corrente(numero_global_conta):
    # usuario pode ter mais de uma conta, mas toda conta deve pertencer a somente um user
    conta = {
        'agencia' : '0001',
        'n_conta' : numero_global_conta,
        'saldo' : 0,
        'limite' : 500,
        'extrato' : "",
        'numero_saques' : 0,
        'limite_saques' : 3,
    }

    return conta