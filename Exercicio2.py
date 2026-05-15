def conta(c) :
    if(c <= 5): return 50
    elif(c>5 and c<=10): return 50+(10*(c-5))
    elif(c>10): return c*5


def pa(a,b,c):
    return ((b+a==c or c+a==b) or
            (a+b==c or c+b==a) or
            (a+c==b or b+c==a))

def pg(a,b,c):
    return ((b*a==c or c*a==b) or
            (a*b==c or c*b==a) or
            (a*c==b or b*c==a))

def pag(a,b,c): return pa(a,b,c) or pg(a,b,c)
