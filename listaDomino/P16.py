# P16: Escreva a função tira_maior_v que associe um valor e uma "mão"
# à lista similar à "mão" de onde se extraiu a pedra de
# maior pontos de um determinado valor para ponta.


def somaDePedras(pedra):
    return pedra[0] + pedra[1]


def tira_maior_v(valor, mao):
    return [pedra for pedra in mao if somaDePedras(pedra) <= valor]
