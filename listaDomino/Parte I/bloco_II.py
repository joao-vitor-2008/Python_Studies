from functools import reduce


def pert(x, a, b):
    return a <= x <= b


def soma_valor_de_pedras(p):
    return p[0] + p[1]


def inverter_pedra(p):
    return (p[1], p[0])


def e_carroca(p):
    return p[0] == p[1] and pedrap(p)


def soma(a, b):
    return a + b


def maior_pedra_mao(mao):
    return reduce(maior_d_2_pedra, mao)


def maior_d_2_pedra(x, y):
    (x1, x2) = x
    (y1, y2) = y
    if soma(x1, x2) > soma(y1, y2):
        return x
    else:
        return y


# Funções extras =======================================================


def pedrap(pedra):
    (p1, p2) = pedra
    return pert(p1, 0, 6) and pert(p2, 0, 6)


def maop(mao):
    mao_valida = [p for p in mao if pedrap(p)]
    return 0 <= len(mao_valida) <= 7 and len(mao_valida) == len(mao)


def carrocap(pedra):
    (p1, p2) = pedra
    return p1 == p2 and pedrap(pedra)


def tem_carroca_p(mao):
    return len([p for p in mao if (p[0] == p[1]) and pedrap(p)]) > 0


def tem_carrocas(mao):
    return [p for p in mao if (p[0] == p[1]) and pedrap(p)]


# Bloco I ======================================================


# p6
def pontos(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        return reduce(soma, lista_pontos)
    else:
        return -999


def garagem(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        pontos = reduce(soma, lista_pontos)
        return pontos - (pontos % 5)
    else:
        return -999


def pedra_igual_p(p1, p2):
    if pedrap(p1) and pedrap(p2):
        (x1, y1) = p1
        (x2, y2) = p2

        return (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2)
    else:
        return False


# P09
def ocorre_pedra_p(p, mao):
    return p in mao or inverter_pedra(p) in mao and pedrap(p) and maop(mao)


# P10
# P10: Escreva a função ocorre_valor_p que associe um valor válido para "ponta" e
# uma "mão" e produza True sss o valor ocorre em alguma pedra da mão e False caso contrário.
def ocorre_valor_p(valor, mao):
    if maop(mao):
        return len([p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)]) > 0
    else:
        return False


# P11
# P11: Escreva a função ocorre_pedra que associe a um valor e uma "mão",
# uma lista contendo as pedras da "mão" que possuem o valor dado.
def ocorre_pedra(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return [p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)]
    else:
        return []


# P12: Escreva a função pedra_maior que associe uma "mão" a
# pedra de maior valor na "mão" dada. Uma pedra p1 é maior que
# uma outra p2 sss a soma das pontas de p1 for maior
# que a soma das pontas de p2.
def pedra_maior(mao):
    if maop(mao):
        return maior_pedra_mao(mao)
    else:
        return -999


# P13: Escreva a função ocorre_valor_q que
# associe um valor e uma "mão" e produza o
# número de pedras na mão que possuem o valor dado.
def ocorre_valor_q(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return len([p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)])
    else:
        return -999


# P14: Escreva a função ocorre_carroca_q que
# associe uma mão à quantidade de carroças nela existentes.
def ocorre_carroca_q(mao):
    if maop(mao):
        return len([p for p in mao if e_carroca(p)])
    else:
        return -999


# P15: Escreva a função tira_maior que associe uma mão a uma
# lista similar à "mão" de onde foi extraída a pedra de maior ponto.
def tira_maior(mao):
    if maop(mao):
        maior_pedra = pedra_maior(mao)
        return [p for p in mao if p != maior_pedra]
    else:
        return []


# P16: Escreva a função tira_maior_v que associe
# um valor e uma "mão" à lista similar à "mão" de
# onde se extraiu a pedra de maior pontos de um
# determinado valor para ponta.
def tira_maior_v(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return [p for p in mao if soma_valor_de_pedras(p) <= valor]
    else:
        return []
