# P09: Escreva a função ocorre_pedra_p que associe uma "pedra" e
# uma "mão" a True sss a "pedra" ocorre na "mão" e False caso contrário.


def ocorre_pedra_p(pedra, mao):
    pedraInversa = (pedra[1], pedra[0])
    return pedra in mao or pedraInversa in mao
