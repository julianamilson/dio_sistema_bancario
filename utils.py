def posicao_cpf(usuarios, id):
    pos = 0
    if not usuarios:
        return -42
    for usuario in usuarios:
        if id == int(usuario[0]):
            return pos
        pos += 1
    return -42