# P15: Escreva a função tira_maior que associe uma mão a uma
# lista similar à "mão" de onde foi extraída a pedra de maior ponto.


def somaDePontas(pedra):
    return pedra[0] + pedra[1]


def pedra_maior(mao):
    maiorPedra = (0, 0)
    for pedra in mao:
        if somaDePontas(pedra) > somaDePontas(maiorPedra):
            maiorPedra = pedra
    return maiorPedra


def tira_maior(mao):
    maiorPedra = pedra_maior(mao)
    return mao.remove(maiorPedra)
