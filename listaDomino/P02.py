def pert(x, a, b):
    return a <= x <= b


def maop(mao):
    mao = [pedra for pedra in mao if pert(pedra[0], 0, 6) and pert(pedra[1], 0, 6)]
     return pert(len(mao), 0, 7) and mao!=[]: