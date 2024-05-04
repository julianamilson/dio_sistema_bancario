def saque(saldo, valor, extrato, limite, numero_saques, limite_saques): #keyword only
    if numero_saques < limite_saques:
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite: 
            print("Operação falhou! O valor do saque excede o limite.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Operação falhou! Número máximo de saques excedido.")

    return saldo, extrato, numero_saques