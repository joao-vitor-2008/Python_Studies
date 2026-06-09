from functools import reduce


def soma_valor_de_pedras(p):
    return p[0] + p[1]


def pontos(mao):
    pontos = 0
    for p in mao:
        pontos += soma_valor_de_pedras(p)
    return pontos


def garagem(mao):
    pontos = 0
    for pedra in mao:
        pontos += pedra[0] + pedra[1]
    return pontos - (pontos % 5)


def pedra_igual_p(pedraUm, pedraDois):
    (x1, y1) = pedraUm
    (x2, y2) = pedraDois

    return (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2)


def ocorre_pedra_p(pedra, mao):
    pedraInversa = (pedra[1], pedra[0])
    return pedra in mao or pedraInversa in mao


def ocorre_valor_p(valor, mao):
    return len([valor for pedra in mao if (pedra[0] + pedra[1]) == valor]) > 0


def ocorre_pedra(valor, mao):
    return [pedra for pedra in mao if (pedra[0] + pedra[1]) == valor]


def pedra_maior(mao):
    maiorPedra = (0, 0)
    for pedra in mao:
        if somaDePontas(pedra) > somaDePontas(maiorPedra):
            maiorPedra = pedra
    return maiorPedra


def ocorre_valor_q(valor, mao):
    counter = 0
    for pedra in mao:
        if valor == somaDePedras(pedra):
            counter += 1
    return counter


def e_carroca(pedra):
    return pedra[0] == pedra[1]


def ocorre_carroca_q(mao):
    counter = 0
    for pedra in mao:
        if e_carroca(pedra):
            counter += 1
    return counter


# P15: Escreva a função tira_maior que associe uma mão a uma
# lista similar à "mão" de onde foi extraída a pedra de maior ponto.


def tira_maior(mao):
    maiorPedra = pedra_maior(mao)
    return mao.remove(maiorPedra)


def tira_maior_v(valor, mao):
    return [pedra for pedra in mao if somaDePedras(pedra) <= valor]
