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
