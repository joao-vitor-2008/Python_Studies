from functools import reduce


# Fuções Extras:
def pert(x, a, b):
    return a <= x <= b


def pedrap(p):
    if len(p) != 2:
        return False
    (p1, p2) = p
    return pert(p1, 0, 6) and pert(p2, 0, 6)


def e_carroca(p):
    return p[0] == p[1]


def sum(a, b):
    return a + b


def valor_p(p):
    return p[0] + p[1]


def valor_pt(pt):
    if pt == []:
        return 0
    if len(pt) == 1:
        return pt[0]
    if len(pt) == 2:
        return sum(pt[0], pt[1])


def tail(xs):
    return xs[1:]


def head(xs):
    return xs[0]


def checar_se_todos_verdadeiros(lista_booleanos):
    return len([item for item in lista_booleanos if item]) == len(lista_booleanos)


def sum_pontos_pt(pt):
    return reduce(sum, [valor_p(p) for p in pt])


mesa = [[(2, 2)], [(5, 2)], [(5, 5), (5, 6), (6, 2)], [(0, 2)], [(5, 4), (4, 2)]]
pt1 = [(5, 5), (5, 6), (6, 2)]
p = (2, 5)


# =================================================================


def lista_de_jogadas(mesa):
    # Pareamos a pedra atual com a próxima usando o zip.
    # Ex: se a lista é [A, B, C], o zip combina (A, B) e (B, C).
    pares_de_pedras = zip(mesa, mesa[1:])

    # A list comprehension desestrutura cada par e checa a regra:
    # O segundo número da pedra atual [1] deve ser igual ao primeiro da próxima [0].
    validacoes = [atual[1] == proxima[0] for atual, proxima in pares_de_pedras]

    # Passamos a lista de True/False para a nossa função auxiliar
    return checar_se_todos_verdadeiros(validacoes)


# P28: Escreva a função mesa2p que associa um valor com True, sss ele representa
# corretamentamente a descrição de uma mesa no formato 2 com sua representação no formato 1.
def mesa2p(mesa):
    return False not in [True for pt in tail(mesa) if lista_de_jogadas(pt + head(mesa))]


# P29: Escreva a função marca_ponto_2 que associa uma mesa no formato 2 com o
# número de pontos marcados.
def marca_ponto_2(mesa):
    total_pontos = reduce(
        sum, [sum_pontos_pt(pt + head(mesa)) for pt in mesa]
    ) - 3 * valor_p(head(head(mesa)))
    if total_pontos % 5 == 0:
        return total_pontos
    else:
        return 0


# P30: Escreva a função faz_jogada_2 que associa uma pedra, uma mesa e
# um número de ponta na mesa, com a mesa obtida após jogar a pedra na ponta indicada.
def index(obj, xs):
    [i for i in range(0, len(xs)) if obj == xs[i]]


def faz_jogada_2(p, mesa, i):
    pt = mesa[i]
    new_pt = [p] + pt
    mesa[i] = new_pt
    return mesa


# P31: Escreva a função pedra_de_ponto que associa uma mesa no formato 1
# com uma pedra que pode marcar ponto.
def pedras_de_ponto(mesa1):


# P32: Escreva a função pedras_de_ponto que associa uma mesa no formato
# 1 com a lista de pedras que podem marcar ponto.

# P33: Escreva a função pedra_de_maior_ponto que associa uma mesa no formato
# 1 com a pedra que marcar mais pontos.

# P34: Escreva a função pedras_fora_p que associa uma mesa no formato 2 e
# uma pedra com True sss ela ainda não foi jogada.
