# P18: Escreva a função carroca_m_p que associe
# uma mesa a True sss pelo menos uma das pontas
# for carroça.


def carroca_m_p(mesa):
    for pedra in mesa:
        if len(pedra) == 2:
            if pedra[0] == pedra[1]:
                return True
    return False
