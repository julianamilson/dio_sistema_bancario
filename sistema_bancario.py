from dentro_conta import dentro_conta as conta
from criar_usuario import criar_usuario
from utils import posicao_cpf

menu_entrada = """
Escolha uma ação
[1] Entrar em conta
[2] Criar conta
[0] Sair
===> """

menu_erro_usuario = """
Usuário inexistente!

Gostaria de criar uma conta?
[1] Sim
[2] Não
===> """

usuarios = []

while True:
    opcao_entrada = input(menu_entrada)
    if opcao_entrada == '1':
        id = int(input("Digite id de usuário: "))
        cpf = posicao_cpf(usuarios, id)
        if cpf == -42:
            opcao = int(input(menu_erro_usuario))
            if opcao == 1:
                novo_usuario = criar_usuario(usuarios)
                if novo_usuario != None:
                    usuarios.append(novo_usuario)
                print(usuarios)
        else:
            conta(usuarios[cpf])
    elif opcao_entrada == '2':
        novo_usuario = criar_usuario(usuarios)
        if novo_usuario != None:
            usuarios.append(novo_usuario)
        print(usuarios)
    elif opcao_entrada == '0':
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")