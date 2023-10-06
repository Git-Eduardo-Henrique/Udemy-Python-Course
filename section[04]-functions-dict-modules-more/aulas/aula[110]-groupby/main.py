from itertools import groupby

def ordernar(aluno):
    return aluno["nota"]

alunos = [
    {"nome": "Beto", "nota": "C"},
    {"nome": "Eduardo", "nota": "A"},
    {"nome": "Tatiana", "nota": "B"},
    {"nome": "Cleiton", "nota": "A"},
    {"nome": "Alfredo", "nota": "B"},
]

alunos_ordenados = sorted(alunos, key=ordernar)
# ordena os items por chave
grupos = groupby(alunos_ordenados, key=ordernar)


for key, value in grupos:
    print("\033[34m", 30 * "=-=", "\033[m")
    print(f"alunos com nota: {key}")
    print("\033[34m", 30 * "=-=", "\033[m")
    for aluno in value:
        print(aluno)

print("\033[34m", 30 * "=-=", "\033[m")