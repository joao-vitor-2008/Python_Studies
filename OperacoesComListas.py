def take(k, xs):
    return xs[:-k]


def drop(k, xs):
    return xs[k:]


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def last(xs):
    return xs[len(xs) - 1]


def init(xs):
    return xs[:-1]


# Dado uma lista de triplas contendo o número de matrícula,
# a nota final (0-10) e a frequência (0-100) de alunos de certa
# disciplina, defina a função aprov(nfs) cuja avaliação associe
# uma lista de tuplas dos alunos aprovados.


def aprov(nfs):
    [aluno for aluno in nfs if (aluno[1] >= 5) and (aluno[2] >= 75)]


# Dado uma lista de triplas contendo o número de matrícula,
# a nota final (0-10) e a frequência (0-100) de alunos de certa
# disciplina, defina a função rfinal(nfs) cuja avaliação associe
# uma tupla formada por 4 inteiros onde: o primeiro representa
# a quantidade de alunos aprovados, o segundo a quantidade de alunos
# reprovados por nota, o terceiro a quantidade de alunos reprovados por falta,
# e o quarto a quantidade de alunos reprovados por nota e por falta.


def aprovado(aluno):
    (matricula, nota, frequência) = aluno
    return (nota >= 5) and (frequência >= 75)


def reprovadoNota(aluno):
    (matricula, nota, frequência) = aluno
    return nota < 5


def reprovadoFalta(aluno):
    (matricula, nota, frequência) = aluno
    return frequência < 75


def rfinal(nfs):
    aprovados = 0
    reprovadosNota = 0
    reprovadosFalta = 0
    reprovadosNotaFalta = 0

    for aluno in nfs:
        if aprovado(aluno):
            aprovados += 1
        elif reprovadoNota(aluno) and reprovadoFalta(aluno):
            reprovadosNotaFalta += 1
        elif reprovadoNota(aluno):
            reprovadosNota += 1
        elif reprovadoFalta(aluno):
            reprovadosFalta += 1
