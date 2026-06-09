def pedrap(pedra):
    (p1, p2) = pedra
    return pert(p1, 0, 6) and pert(p2, 0, 6)


def pert(x, a, b):
    return a <= x <= b


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
