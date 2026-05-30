from functools import reduce as reduce

# e1: Dado uma lista 'nfs' de triplas, cada uma contendo o número de matrícula, a nota final (0-10)
# e a frequência (0-100) de alunos de certa disciplina, defina a função max(nfs) cuja avaliação
# associe a tupla com nota de maior valor. Use a definição por compreensão.

def maiores(x,xs): return [y for y in xs if y>x]

def maiorais(xs):
    return [ k for k in xs if maiores(k,xs)==[] ]

def maiornota(xs):
    return maiorais(xs)[0]

def notas(nfs): return [ aluno[1] for aluno in nfs ]

def max(nfs):
    return[aluno for aluno in nfs if aluno[1]==maiornota(notas(nfs))]



# e2: Dado uma lista 'nfs' de triplas, cada uma contendo o número de matrícula, a nota final (0-10) 
# e a frequência (0-100) de alunos de certa disciplina, defina a função min(nfs) cuja avaliação
# associe a tupla com nota de menor valor. Use a função 'reduce' (paradigma aplicativo).i

def menor(x, y): 
    if x <= y: return x
    else : return y

def min(nfs): return [aluno for aluno in nfs if aluno[1] == reduce(menor,notas(nfs))]
