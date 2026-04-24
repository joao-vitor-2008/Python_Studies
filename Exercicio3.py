def DeltaA(a1, a2):
    return a1 - a2


def Notpert(x, a, b):
    return not (x >= a and x <= b)


def Modulo(a):
    if a <= 0:
        return a * (-1)
    else:
        return a


def possivel(x1, y1, x2, y2):
    if Notpert(x1, 1, 8) or Notpert(y1, 1, 8) or Notpert(x2, 1, 8) or Notpert(y2, 1, 8):
        return False

    if (
        Modulo(DeltaA(x1, x2)) / Modulo(DeltaA(y1, y2)) == 2
        or Modulo(DeltaA(x1, x2)) / Modulo(DeltaA(y1, y2)) == 0.5
    ):
        return True
    else:
        return False
