from functools import reduce


def pert(x, a, b):
    return a <= x <= b


def e_carroca(p):
    return p[0] == p[1]


def sum(a, b):
    return a + b


def valor_pt(pt):
    if pt == []:
        return 0
    if len(pt) == 1:
        return pt[0]
    if len(pt) == 2:
        return sum(pt[0], pt[1])


def onde_pode_jogar(p, mesa):
    return [mesa.index(pt) for pt in mesa if p[0] in pt or p[1] in pt]


def head(xs):
    return xs[0]


def sub_p_in_mesa(p, mesa):
    mesa_l = list(mesa)

    jogadas = onde_pode_jogar(p, mesa)
    primeira_jogada = head(jogadas)

    index_p = p.index(head(mesa[primeira_jogada]))

    if index_p == 1:
        mesa_l[primeira_jogada] = [p[0]]
    else:
        mesa_l[primeira_jogada] = [p[1]]
    return tuple(mesa_l)


def subt_p_i(p, mesa):
    return [
        (pontos_marcados(joga_pedra(p, mesa, i)), i) for i in onde_pode_jogar(p, mesa)
    ]


def subt_p_from_mao_in_mesa(p, mesa, mao):
    return [
        (pontos_marcados(joga_pedra(p, mesa, i)), i, mao.index(p))
        for i in onde_pode_jogar(p, mesa)
    ]


def subt_p_from_i_in_mesa(tp, mao, mesa):
    (index_mesa, index_mao) = tp
    mesa_l = list(mesa)

    p = mao[index_mao]

    jogadas = onde_pode_jogar(p, mesa)
    primeira_jogada = head(jogadas)

    index_p = p.index(head(mesa[primeira_jogada]))

    if index_p == 1:
        mesa_l[index_mesa] = [p[0]]
    else:
        mesa_l[index_mesa] = [p[1]]

    return tuple(mesa_l)


# ==========================================================================================


# P17
def mesap(mesa):
    return (
        len(
            [
                pt
                for pt in mesa
                if (len(pt) == 0)
                or (len(pt) == 1 and pert(pt[0], 0, 6))
                or (len(pt) == 2 and e_carroca(pt) and pert(pt[0], 0, 6))
            ]
        )
        == 4
        and len(mesa) == 4
    )


# P18
def carroca_m_p(mesa):
    return [pt for pt in mesa if len(pt) == 2 and e_carroca(pt)] != []


# P19
def pontos_marcados(mesa):
    pontos_mesa = reduce(sum, [valor_pt(pt) for pt in mesa])
    if pontos_mesa is None:
        return 0
    if pontos_mesa % 5 == 0:
        return pontos_mesa
    else:
        return 0


# P20
def pode_jogar_p(p, mesa):
    return [pt for pt in mesa if p[0] in pt or p[1] in pt] != []


# P21
def marca_ponto_p(p, mesa):
    pontos = subt_p_i(p, mesa)
    return [head(pt) for pt in pontos if head(pt) != 0] != []


# P22
def maior_ponto(p, mesa):
    return max(subt_p_i(p, mesa))[1]


# P23
def joga_pedra(p, mesa, i):
    mesa_l = list(mesa)
    pt_atual = mesa[i]

    if len(pt_atual) == 0:
        if p[0] == p[1]:
            mesa_l[i] = [p[0], p[1]]
        else:
            mesa_l[i] = [p[0]]
    else:
        val_mesa = pt_atual[0]
        if p[0] == val_mesa:
            novo_lado = p[1]
        else:
            novo_lado = p[0]

        if p[0] == p[1]:
            mesa_l[i] = [p[0], p[1]]
        else:
            mesa_l[i] = [novo_lado]
    return tuple(mesa_l)


# P24
def jogap(mao, mesa):
    return [p for p in mao if pode_jogar_p(p, mesa)] != []


# P25
def jogada(mao, mesa):
    maior_jogada = max(max([subt_p_from_mao_in_mesa(p, mesa, mao) for p in mao]))
    return (maior_jogada[1], maior_jogada[2])


# P26
def faz_jogada(mao, mesa):
    return subt_p_from_i_in_mesa(jogada(mao, mesa), mao, mesa)
