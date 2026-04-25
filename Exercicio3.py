# Função que retorna a diferença entre dois numeros
def DeltaA(a1, a2):
    return a1 - a2


# Função que verifica se um numero não pertence a um intervalo fechado de a e b
def Notpert(x, a, b):
    return not (x >= a and x <= b)


def possivel(x1, y1, x2, y2):
    # Se pelo menos um dos elementos estiver fora do tabuleiro a funçao retorna False
    # É possivel enxugar mais o código e diminuir o número de funcões, porém deu preguiça.
    if Notpert(x1, 1, 8) or Notpert(y1, 1, 8) or Notpert(x2, 1, 8) or Notpert(y2, 1, 8):
        return False

    # Os movimentos possiveis de um cavalo dentro de um tabuleiro sempre seguem o mesmo padrão,
    # é um par ordenado {2,1} ou {1,2}, se for diferente disso não caracteriza um movimento possivel
    # abs retorna o valor absoluto do número. abs(-5) = 5
    if (abs(DeltaA(x1, x2)) == 2 and abs(DeltaA(y1, y2)) == 1) or (
        abs(DeltaA(x1, x2)) == 1 and abs(DeltaA(y1, y2)) == 2
    ):
        return True
    else:
        return False
