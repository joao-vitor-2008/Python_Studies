# P10: Escreva a função ocorre_valor_p que associe um valor válido para "ponta"
# e uma "mão" e produza True sss o valor ocorre em alguma pedra da mão e False caso contrário


def ocorre_valor_p(valor, mao):
    return len([valor for pedra in mao if (pedra[0] + pedra[1]) == valor]) > 0
