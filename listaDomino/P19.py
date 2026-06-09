# P19: Escreva a função pontos_marcados que associe uma
# mesa ao o número de pontos a serem marcados se
# a soma das pontas for múltiplo de cinco e zero em caso
# contrário.


from P17 import mesap


def pontos_marcados(mesa):
    if mesap(mesa):
        somaDasPontas = 0
        for pedra in mesa:
            if len(pedra) == 2:
                somaDasPontas += pedra[0] + pedra[1]
            else:
                somaDasPontas += pedra[0]
        if (somaDasPontas == 0) or (somaDasPontas % 5 != 0):
            return 0
        else:
            return somaDasPontas
