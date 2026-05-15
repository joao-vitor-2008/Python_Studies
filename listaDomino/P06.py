def pontos(mao):
    pontos = 0
    for pedra in mao:
        pontos += pedra[0] + pedra[1]
    return pontos
