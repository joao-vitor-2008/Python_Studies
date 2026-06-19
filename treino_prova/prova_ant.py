def dvz(x):
    return [y for y in range(1, x + 1) if x % y == 0]


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def qtd_list(x, ys):
    return len([y for y in ys if x == y])


def ctg(ks, xs):
    return [(k, qtd_list(k, xs)) for k in ks]


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def inverter_pedra(p):
    return (p[1], p[0])


def fora(mesa, p):
    return not (p in mesa or inverter_pedra(p) in mesa)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def luz(u, c):
    consumo_bruto = u * c
    if consumo_bruto < 200:
        return consumo_bruto * 0.7
    if 1000 < consumo_bruto < 1500:
        return consumo_bruto * 1.2
    if consumo_bruto > 1500:
        return consumo_bruto * 1.5
