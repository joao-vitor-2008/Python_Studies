from functools import reduce

# Funções Auxiliares Comuns e Utilitárias =============================


def pert(x, a, b):
    return a <= x <= b


def soma(a, b):
    return a + b


def sum(a, b):
    return a + b


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def index(obj, xs):
    [i for i in range(0, len(xs)) if obj == xs[i]]


def checar_se_todos_verdadeiros(lista_booleanos):
    return len([item for item in lista_booleanos if item]) == len(lista_booleanos)


# Funções de Manipulação e Validação de Pedras =======================


def pedrap(pedra):
    if len(pedra) != 2:
        return False
    (p1, p2) = pedra
    return pert(p1, 0, 6) and pert(p2, 0, 6)


def soma_valor_de_pedras(p):
    return p[0] + p[1]


def valor_p(p):
    return p[0] + p[1]


def inverter_pedra(p):
    return (p[1], p[0])


def e_carroca(p):
    return p[0] == p[1] and pedrap(p)


def carrocap(pedra):
    (p1, p2) = pedra
    return p1 == p2 and pedrap(pedra)


def maior_d_2_pedra(x, y):
    (x1, x2) = x
    (y1, y2) = y
    if soma(x1, x2) > soma(y1, y2):
        return x
    else:
        return y


def pedra_igual_p(p1, p2):
    if pedrap(p1) and pedrap(p2):
        (x1, y1) = p1
        (x2, y2) = p2
        return (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2)
    else:
        return False


# Funções de Manipulação de Mão ======================================


def maop(mao):
    mao_valida = [p for p in mao if pedrap(p)]
    return 0 <= len(mao_valida) <= 7 and len(mao_valida) == len(mao)


def maior_pedra_mao(mao):
    return reduce(maior_d_2_pedra, mao)


def tem_carroca_p(mao):
    return len([p for p in mao if (p[0] == p[1]) and pedrap(p)]) > 0


def tem_carrocas(mao):
    return [p for p in mao if (p[0] == p[1]) and pedrap(p)]


# Funções de Pontas da Mesa ==========================================


def valor_pt(pt):
    if len(pt) == 1:
        return pt[0]
    if len(pt) == 2:
        return sum(pt[0], pt[1])
    else:
        return 0


def sum_pontos_pt(pt):
    return reduce(sum, [valor_p(p) for p in pt])


def onde_pode_jogar(p, mesa):
    return [mesa.index(pt) for pt in mesa if p[0] in pt or p[1] in pt]


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


# Bloco I (P06 a P16) =================================================


# P06
def pontos(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        return reduce(soma, lista_pontos)
    else:
        return -999


def garagem(mao):
    if maop(mao):
        lista_pontos = [soma_valor_de_pedras(p) for p in mao if pedrap(p)]
        pontos = reduce(soma, lista_pontos)
        return pontos - (pontos % 5)
    else:
        return -999


# P09
def ocorre_pedra_p(p, mao):
    return p in mao or inverter_pedra(p) in mao and pedrap(p) and maop(mao)


# P10
def ocorre_valor_p(valor, mao):
    if maop(mao):
        return len([p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)]) > 0
    else:
        return False


# P11
def ocorre_pedra(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return [p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)]
    else:
        return []


# P12
def pedra_maior(mao):
    if maop(mao):
        return maior_pedra_mao(mao)
    else:
        return -999


# P13
def ocorre_valor_q(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return len([p for p in mao if valor == p[0] or valor == p[1] and pedrap(p)])
    else:
        return -999


# P14
def ocorre_carroca_q(mao):
    if maop(mao):
        return len([p for p in mao if e_carroca(p)])
    else:
        return -999


# P15
def tira_maior(mao):
    if maop(mao):
        maior_pedra = pedra_maior(mao)
        return [p for p in mao if p != maior_pedra]
    else:
        return []


# P16
def tira_maior_v(valor, mao):
    if maop(mao) and pert(valor, 0, 6):
        return [p for p in mao if soma_valor_de_pedras(p) <= valor]
    else:
        return []


# Bloco II (P17 a P26 - Formato Mesa 1) ===============================


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


# Bloco III (P27 a P34 - Formato Mesa 2) ==============================


# P27
def lista_de_jogadas(mesa):
    pares_de_pedras = zip(mesa, mesa[1:])
    validacoes = [atual[1] == proxima[0] for atual, proxima in pares_de_pedras]
    return checar_se_todos_verdadeiros(validacoes)


# P28
def mesa2p(mesa):
    return False not in [True for pt in tail(mesa) if lista_de_jogadas(pt + head(mesa))]


# P29
def marca_ponto_2(mesa):
    total_pontos = reduce(
        sum, [sum_pontos_pt(pt + head(mesa)) for pt in mesa]
    ) - 3 * valor_p(head(head(mesa)))
    if total_pontos % 5 == 0:
        return total_pontos
    else:
        return 0


# P30
def faz_jogada_2(p, mesa, i):
    pt = mesa[i]
    new_pt = [p] + pt
    mesa[i] = new_pt
    return mesa


# P31: Escreva a função pedra_de_ponto que
# associa uma mesa no formato 1 com uma
# pedra que pode marcar ponto.
def pontos_mesa1(mesa1):
    v_bruto = [valor_pt(pt) for pt in mesa1]
    v_limpo = [0 if v is None else v for v in v_bruto]
    return reduce(sum, v_limpo)


def m5_maior(x):
    i = x // 5
    return (i + 1) * 5


def pedra_de_ponto(mesa1):
    pontos_atuais = pontos_mesa1(mesa1)
    if pontos_atuais % 5 == 0:
        faltam = 5
    else:
        faltam = m5_maior(pontos_atuais) - pontos_atuais

    candidatos = [
        (valor_pt(pt), valor_pt(pt) + faltam)
        for pt in mesa1
        if valor_pt(pt) + faltam <= 6 and pt != []
    ]

    if candidatos != []:
        return head(candidatos)
    else:
        return (0, 0)


# P32: Escreva a função pedras_de_ponto que associa
# uma mesa no formato 1 com a lista de pedras
# que podem marcar ponto.
def pedras_de_ponto(mesa1):
    pontos_atuais = pontos_mesa1(mesa1)
    if pontos_atuais % 5 == 0:
        faltam = 5
    else:
        faltam = m5_maior(pontos_atuais) - pontos_atuais

    candidatos = [
        (valor_pt(pt), valor_pt(pt) + faltam)
        for pt in mesa1
        if valor_pt(pt) + faltam <= 6 and pt != []
    ]

    if candidatos != []:
        return candidatos
    else:
        return (0, 0)


# P33: Escreva a função pedra_de_maior_ponto que
# associa uma mesa no formato 1 com a pedra que
# marcar mais pontos.
def meu_max(lista):
    if not lista:
        return (0, 0)
    else:
        return [x for x in lista if not [y for y in lista if y > x]][0]


def pedra_de_maior_ponto(mesa1):
    candidatas = [(subt_p_i(p, mesa1), p) for p in pedras_de_ponto(mesa1)]
    if candidatas == (0, 0) or not candidatas:
        return (0, 0)
    return meu_max(candidatas)[1]


# P34: Escreva a função pedras_fora_p que associa
# uma mesa no formato 2 e uma pedra com True sss
# ela ainda não foi jogada.
def pedras_fora_p(mesa2, p):
    return [
        ped for pt in mesa2 for ped in pt if ped == p or ped == inverter_pedra(p)
    ] == []


# Variáveis globais de teste originais ================================
mesa2 = [[(2, 2)], [(5, 2)], [(5, 5), (5, 6), (6, 2)], [(0, 2)], [(5, 4), (4, 2)]]
mesa1 = ([5], [5, 5], [0], [4])
pt1 = [(5, 5), (5, 6), (6, 2)]
p = (0, 0)
