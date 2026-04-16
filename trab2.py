import math


def xp(n):
    return (n > 0 and n <= 100) and (n % 3 == 0) and (n % 5 == 0)


def Amarelo(x1, x2, y1, y2):
    deltaY = y1 - y2

    sqrSide = (deltaY * math.sqrt(2)) / 2

    sqrArea = sqrSide * sqrSide

    circleRadius = sqrSide / 2

    circleArea = math.pi * (circleRadius * circleRadius)

    areaAmarela = sqrArea - circleArea

    return areaAmarela
