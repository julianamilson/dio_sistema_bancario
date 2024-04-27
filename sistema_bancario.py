menu = """
Escolha uma acao

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":

        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Informe o valor do saque: "))

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


    elif opcao == "3":
        print("EXTRATO".center(50, '=')
              +("Não foram realizadas movimentações." if not extrato else extrato)
              +f"Saldo: R$ {saldo:.2f}" + "EXTRATO".center(50, '=')
              )

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")