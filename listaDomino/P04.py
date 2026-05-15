def tem_carroca_p(mao):
    carrocas = [pedra for pedra in mao if (pedra[0] == pedra[1])]
    if len(carrocas) > 0:
        return True
    else:
        return False
