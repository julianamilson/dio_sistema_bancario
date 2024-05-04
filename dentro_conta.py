from criar_conta_corrente import criar_conta_corrente
from deposito import deposito
from extrato import extrato as f_extrato
from saque import saque

_menu_conta = """
Escolha uma ação

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar conta corrente
[0] Sair
=> """

def pegar_valor(funcao=""):
    return float(input(f"Informe o valor do {funcao}: "))

def pegar_contas(contas):
    i = 0
    for conta in contas:
        i += 1
    return i

def dentro_conta(usuario, contas_bancarias):
    while True:
        opcao = input(_menu_conta)
        tem_conta_corrente = pegar_contas(usuario[1]["contas_correntes"])
        if tem_conta_corrente > 0:
            indice = usuario[1]["contas_correntes"][0] - 1
            aux_conta_update = contas_bancarias[indice][1]

        if (opcao == '1' or opcao == '2' or opcao == '3') and tem_conta_corrente == 0:
            print("Usuário não tem conta corrente.")

        elif opcao == '4':
                numero_conta = len(contas_bancarias) + 1
                nova_conta = criar_conta_corrente(numero_conta)
                aux = [usuario[0], nova_conta]
                contas_bancarias.append(aux)
                usuario[1]["contas_correntes"].append(numero_conta)
                tem_conta_corrente = pegar_contas(usuario[1]["contas_correntes"]) + 1

        else:
            indice = usuario[1]["contas_correntes"][0] - 1
            saldo = contas_bancarias[indice][1]['saldo']
            extrato = contas_bancarias[indice][1]['extrato']
            limite = contas_bancarias[indice][1]['limite']
            numero_saques = contas_bancarias[indice][1]['numero_saques']
            limite_saques = contas_bancarias[indice][1]['limite_saques']
    
            if opcao == "1":
                valor = pegar_valor(funcao="depósito")
                saldo, extrato = deposito(saldo, valor, extrato)

            elif opcao == "2":
                valor = pegar_valor(funcao="saque")
                saldo, extrato, numero_saques= saque(saldo, valor, extrato, limite, numero_saques, limite_saques)

            elif opcao == "3":
                f_extrato(saldo, extrato=extrato)

            elif opcao == "0":
                contas_bancarias[indice][1]['saldo'] = saldo
                contas_bancarias[indice][1]['extrato'] = extrato
                contas_bancarias[indice][1]['limite'] = limite
                contas_bancarias[indice][1]['numero_saques'] = numero_saques
                contas_bancarias[indice][1]['limite_saques'] = limite_saques
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

            contas_bancarias[indice][1]['saldo'] = saldo
            contas_bancarias[indice][1]['extrato'] = extrato
            contas_bancarias[indice][1]['limite'] = limite
            contas_bancarias[indice][1]['numero_saques'] = numero_saques
            contas_bancarias[indice][1]['limite_saques'] = limite_saques