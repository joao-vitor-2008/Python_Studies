# P11: Escreva a função ocorre_pedra que associe a um valor e
# uma "mão", uma lista contendo as pedras da "mão" que possuem o valor dado.


def ocorre_pedra(valor, mao):
    return [pedra for pedra in mao if (pedra[0] + pedra[1]) == valor]
