def isCarrao(pedra):
    return pedra[0] == pedra[1]


def ocorre_carroca_q(mao):
    counter = 0
    for pedra in mao:
        if isCarrao(pedra):
            counter += 1
    return counter
