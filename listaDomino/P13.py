# P13: Escreva a função ocorre_valor_q que associe um valor e uma
# "mão" e produza o número de pedras na mão que possuem o valor dado.


def somaDePedras(pedra):
    return pedra[0] + pedra[1]


def ocorre_valor_q(valor, mao):
    counter = 0
    for pedra in mao:
        if valor == somaDePedras(pedra):
            counter += 1
    return counter
