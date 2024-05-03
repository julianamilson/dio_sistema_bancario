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
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def pegar_valor(funcao=""):
    return float(input(f"Informe o valor do {funcao}: "))

def dentro_conta(usuario):
    while True:
        opcao = input(_menu_conta)
        if opcao == "1":
            valor = pegar_valor(funcao="depósito")
            deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = pegar_valor(funcao="saque")
            saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "3":
            f_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            usuario[1]["contas_correntes"].append("bingus")
            print(usuario[1]["contas_correntes"])

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")