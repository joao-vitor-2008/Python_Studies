# P08: Escreva a função pedra_igual_p que associe dois pares de
# inteiros a True sss representam a mesma pedra e False caso contrário.
# É bom lembrar que a ordem das pontas é irrelevante, assim (2,4) e (4,2) representam a mesma pedra.


def pedra_igual_p(pedraUm, pedraDois):
    (x1, y1) = pedraUm
    (x2, y2) = pedraDois

    return (x1 == x2 and y1 == y2) or (x1 == y2 and y1 == x2)
