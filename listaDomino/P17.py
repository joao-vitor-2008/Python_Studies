# P17: Escreva a função mesap que as
# socie uma quadrupla de listas a True
# sss a quadrupla for
# uma descrição válida de "mesa".


def pertIntervaloFechado(x, a, b):
    return a <= x <= b


def mesap(mesa):
    if len(mesa) != 4:
        return False
    for pedra in mesa:
        if not (pedra != []):
            if len(pedra) > 2:
                return False
            if len(pedra) == 2:
                (p1, p2) = pedra
                if p1 != p2:
                    return False
            if not (pertIntervaloFechado(pedra[0], 0, 6)):
                return False

    else:
        return True
