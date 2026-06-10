from functools import reduce


def soma_valor_de_pedras(p):
    return p[0] + p[1]


def inverter_pedra(p):
    return (p[1], p[0])


def e_carroca(p):
    return p[0] == p[1]


def pedrap(pedra):
    (p1, p2) = pedra
    return pert(p1, 0, 6) and pert(p2, 0, 6)


def maop(mao):
    mao_valida = [p for p in mao if pedrap(p)]
    return 0 <= len(mao_valida) <= 7 and len(mao_valida) == len(mao)


def pert(x, a, b):
    return a <= x <= b


def soma(a, b):
    return a + b


# Funções extras


def pontos(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        return reduce(soma, lista_pontos)
    else:
        return (-1, False)


def garagem(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        pontos = reduce(soma, lista_pontos)
        return pontos - (pontos % 5)
    else:
        return (-1, False)


def pedra_igual_p(p1, p2):
    if pedrap(p1) and pedrap(p2):
        (x1, y1) = p1
        (x2, y2) = p2

        return (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2)
    else:
        return (-1, False)


def ocorre_pedra_p(p, mao):
    if maop(mao) and pedrap(p):
        return p in mao or inverter_pedra(p) in mao
    else:
        return (-1, False)


def ocorre_valor_p(valor, mao):
    if maop(mao) and pert(valor, 0, 12):
        return (
            len([p for p in mao if (soma_valor_de_pedras(p) == valor) and pedrap(p)])
            > 0
        )
    else:
        return (-1, False)


def ocorre_pedra(valor, mao):
    if maop(mao) and pert(valor, 0, 12):
        return [p for p in mao if (soma_valor_de_pedras(p) == valor) and pedrap(p)]
    else:
        return (-1, False)


def pedra_maior(mao):
    if maop(mao):
        maior_pedra = (0, 0)
        for pedra in mao:
            if soma_valor_de_pedras(pedra) > soma_valor_de_pedras(maior_pedra):
                maior_pedra = pedra
        return maior_pedra
    else:
        return (-1, False)


def ocorre_valor_q(valor, mao):
    if maop(mao) and pert(valor, 0, 12):
        return len([p for p in mao if (soma_valor_de_pedras(p) == valor) and pedrap(p)])
    else:
        return (-1, False)


def ocorre_carroca_q(mao):
    if maop(mao):
        return len([p for p in mao if e_carroca(p) and pedrap(p)])
    else:
        return (-1, False)


def tira_maior(mao):
    if maop(mao):
        maior_pedra = pedra_maior(mao)
        return [p for p in mao if p != maior_pedra]
    else:
        return (-1, False)


def tira_maior_v(valor, mao):
    if maop(mao) and pert(valor, 0, 12):
        return [p for p in mao if soma_valor_de_pedras(p) <= valor and pedrap(p)]
    else:
        return (-1, False)
