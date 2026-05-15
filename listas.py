def subListaPar(xs):
    return [x**2 for x in xs if x%2==0]


def zeroUm(x):
    if(x**2 < 1000): return 0
    elif(x**2 >= 1000): return 1

def lista(xs):
    return [zeroUm(x) for x in xs if x%2==0]
