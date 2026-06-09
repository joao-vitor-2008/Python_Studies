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
