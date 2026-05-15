def sa(n) :
    mil = n//1000
    RestoDeMil=n%1000
    cent=RestoDeMil//100
    RestoDeCem=RestoDeMil%100
    dez=RestoDeCem//10
    unidade = n%10

    return (mil+cent+dez+unidade)

def pontos(p1,p2):
    a=p1[0]
    b=p1[1]

    if((p1[0] + p2[0])%5==0) : return (p1[0] + p2[0])
