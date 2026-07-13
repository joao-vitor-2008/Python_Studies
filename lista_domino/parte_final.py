def somavet(x, y):
    (x1, x2) = x
    (y1, y2) = y
    return (x1 + y1, x2 + y2)


def sumdo(n):
    return [(x, y) for x in range(n + 1) for y in range(n + 1) if x + y == n and x <= y]


def qt(xs):
    return (len([p for p in xs if p % 2 == 0]), len([p for p in xs if p % 2 == 1]))


def alterna(xs):
    pares = [x for x in xs if x % 2 == 0]
    impares = [x for x in xs if x % 2 == 1]
    if xs[0] % 2 == 0:
        return [z for p, i in zip(pares, impares) for z in (p, i)]
    return [z for i, p in zip(impares, pares) for z in (i, p)]


def intersec(xs, ys):
    if xs == ys:
        return xs
    else:
        return [k for k in xs if ocorre(k, ys)]


def ocorre(k, xs):
    return [x for x in xs if k == x] != []


def uni(xs, ys):
    return xs + [y for y in ys if y not in xs]


def pertence(x, intervalo):
    (a, b) = intervalo
    return x >= a and x <= b


def letra(x):
    return maiuscula(x) or minuscula(x)


def numero(x):
    return pertence(x, (0, 9))


def maiuscula(x):
    return pertence(x, ("A", "Z"))


def minuscula(x):
    return pertence(x, ("a", "z"))


def c_2_l(cadeia):
    return [cadeia[i] for i in range(len(cadeia))]


def e_palav(cadeia):
    return len([c for c in cadeia if letra(c)]) == len(cadeia)


def e_int(cadeia):
    return len([c for c in cadeia if numero(int(c))]) == len(cadeia)


def conjuga(verb, temp):
    terminacao = verb[len(verb) - 2 :]
    radical = verb[:-2]
    pronomes = ["eu ", "tu ", "ele ", "nós ", "vós ", "eles "]

    if temp == "futuro do presente" or temp == "futuro do preterito":
        base = verb
    else:
        base = radical

    presente = [
        ["o", "as", "a", "amos", "ais", "am"],
        ["o", "es", "e", "emos", "eis", "em"],
        ["o", "es", "e", "imos", "is", "em"],
    ]

    perfeito = [
        ["ei", "aste", "ou", "amos", "astes", "aram"],
        ["i", "este", "eu", "emos", "estes", "eram"],
        ["i", "iste", "iu", "imos", "istes", "iram"],
    ]

    imperfeito = [
        ["ava", "avas", "ava", "ávamos", "áveis", "avam"],
        ["ia", "ias", "ia", "íamos", "íeis", "iam"],
        ["ia", "ias", "ia", "íamos", "íeis", "iam"],
    ]

    mais_que_perfeito = [
        ["ara", "aras", "ara", "áramos", "áreis", "aram"],
        ["era", "eras", "era", "êramos", "êreis", "eram"],
        ["ira", "iras", "ira", "íramos", "íreis", "iram"],
    ]

    futuro_presente = [
        ["ei", "ás", "á", "emos", "eis", "ão"],
        ["ei", "ás", "á", "emos", "eis", "ão"],
        ["ei", "ás", "á", "emos", "eis", "ão"],
    ]

    futuro_preterito = [
        ["ia", "ias", "ia", "íamos", "íeis", "iam"],
        ["ia", "ias", "ia", "íamos", "íeis", "iam"],
        ["ia", "ias", "ia", "íamos", "íeis", "iam"],
    ]

    tabs = [
        presente,
        perfeito,
        imperfeito,
        mais_que_perfeito,
        futuro_presente,
        futuro_preterito,
    ]

    tempos = [
        "presente",
        "perfeito",
        "imperfeito",
        "mais_que_perfeito",
        "futuro do presente",
        "futuro do preterito",
    ]

    i = ["ar", "er", "ir"].index(terminacao)

    h = tempos.index(temp)

    return [pronomes[k] + base + tabs[h][i][k] for k in range(6)]


def e_numero(x):
    return len([n for n in x if pertence(ord(n), (48, 57)) and numero(int(n))]) == len(
        x
    )


def e_float(cadeia):
    if "." not in cadeia:
        return False
    i = cadeia.index(".")
    p_parte = cadeia[:i]
    s_parte = cadeia[i + 1 :]
    return p_parte != "" and s_parte != "" and e_numero(p_parte) and e_numero(s_parte)


def int_frac(cadeia):
    if e_numero(cadeia):
        return (cadeia, "0")
    elif e_float(cadeia):
        i = cadeia.index(".")
        p_parte = cadeia[:i]
        s_parte = cadeia[i + 1 :]
        return (p_parte, s_parte)
    else:
        return ("0", "0")


def traduz(numero):
    s_numeros = [
        "zero",
        "um",
        "dois",
        "três",
        "quatro",
        "cinco",
        "seis",
        "sete",
        "oito",
        "nove",
        "dez",
        "onze",
        "doze",
        "treze",
        "quatorze",
        "quinze",
        "desesseis",
        "desesete",
        "desoito",
        "desenove",
    ]
    d_numeros = [
        "vinte",
        "trinta",
        "quarenta",
        "cinquenta",
        "sessenta",
        "setenta",
        "oitenta",
        "noventa",
    ]

    if 0 <= numero < 20:
        return s_numeros[numero]
    elif numero > 19 and numero < 100:
        if numero % 10 == 0:
            return d_numeros[(numero // 10) - 2]
        else:
            return d_numeros[(numero // 10) - 2] + " e " + traduz(numero % 10)
    else:
        return "None"
