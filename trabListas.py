def result(alunos):
    return [aprovado(aluno) for aluno in alunos]

def aprovado(aluno):
    (mat,nota) = aluno
    if(nota >= 5): return (mat,"ap")
    else: return (mat,"rp")
