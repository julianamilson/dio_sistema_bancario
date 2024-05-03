def extrato(saldo, extrato=""):  #positional e keyword only  
    print("EXTRATO".center(50, '='))
    if not extrato or not saldo:
        print("Não foram realizadas movimentações.")
    else:
        print(f"Saldo: R$ {saldo:.2f}")
    print("".center(50, '='))