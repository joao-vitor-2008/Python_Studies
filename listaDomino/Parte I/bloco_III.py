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
# P18: Escreva a função carroca_m_p que associe
# uma mesa a True sss pelo menos uma das pontas
# for carroça.


def carroca_m_p(mesa):
    for pedra in mesa:
        if len(pedra) == 2:
            if pedra[0] == pedra[1]:
                return True
    return False
# P19: Escreva a função pontos_marcados que associe uma
# mesa ao o número de pontos a serem marcados se
# a soma das pontas for múltiplo de cinco e zero em caso
# contrário.


from P17 import mesap


def pontos_marcados(mesa):
    if mesap(mesa):
        somaDasPontas = 0
        for pedra in mesa:
            if len(pedra) == 2:
                somaDasPontas += pedra[0] + pedra[1]
            else:
                somaDasPontas += pedra[0]
        if (somaDasPontas == 0) or (somaDasPontas % 5 != 0):
            return 0
        else:
            return somaDasPontas
# P20: Escreva a função pode_jogar_p que associe
# uma "pedra" e uma "mesa" a True sss a pedra
# possui uma ponta que combina com pelo menos
# uma das pontas da mesa.

from P17 import mesap


def onde_pode_jogar_p(pedra, mesa):
    if len(pedra) == 1:
        index_combinacoes = [
            mesa.index(comb)
            for comb in mesa
            if (comb != 0) and ((comb[0] == pedra[0]) or (comb[1] == pedra[0]))
        ]
        return index_combinacoes
    elif len(pedra) == 2:
        (p1, p2) = pedra
        index_combinacoes = [
            mesa.index(comb)
            for comb in mesa
            if (comb != [])
            and (
                ((comb[0] == p1) or (comb[0] == p2))
                or ((comb[1] == p1) or (comb[1] == p2))
            )
        ]
        return index_combinacoes


def pode_jogar_p(pedra, mesa):
    if mesap(mesa):
        if len(onde_pode_jogar_p(pedra, mesa)) != 0:
            return True
# P21: Escreva a função marca_ponto_p que tenha como
# entrada uma "pedra" e uma "mesa" e produza True sss
# a pedra pode ser jogada fazendo pontos em uma das
# pontas da mesa. Lembre-se que as carroças devem ser
# contadas pelas duas pontas da pedra.

from P19 import pontos_marcados
from p20 import pode_jogar_p


def combinacoes(pedra, mesa):
    return [mesa.index(combinacao) for combinacao in mesa if combinacao[0] == pedra[0]]


def replace_pedra(mesa, pedra):
    tup_list = list(mesa)
    tup_list[combinacoes(pedra, mesa)[0]] = pedra
    new_tuple = tuple(tup_list)
    return new_tuple


def jogar(pedra, mesa):
    return replace_pedra(mesa, pedra)


def marca_ponto_p(pedra, mesa):
    if pode_jogar_p(pedra, mesa):
        return pontos_marcados(jogar(pedra, mesa)) != 0
