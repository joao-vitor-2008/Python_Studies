# P12: Escreva a função pedra_maior que associe uma "mão" a pedra de maior valor na "mão" dada. Uma pedra
# p1 é maior que uma outra p2 sss a soma das pontas de p1 for maior que a soma das pontas de p2.


def somaDePontas(pedra):
    return pedra[0] + pedra[1]


def pedra_maior(mao):
    maiorPedra = (0, 0)
    for pedra in mao:
        if somaDePontas(pedra) > somaDePontas(maiorPedra):
            maiorPedra = pedra
    return maiorPedra
