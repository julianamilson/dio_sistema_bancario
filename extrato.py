def extrato(saldo, extrato=""):  #positional e keyword only  
    print("EXTRATO".center(50, '=')
            +("Não foram realizadas movimentações." if not extrato else extrato)
            +f"Saldo: R$ {saldo:.2f}" + "EXTRATO".center(50, '=')
            )