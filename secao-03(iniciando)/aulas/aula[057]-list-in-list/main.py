salas = [
    ["Eduardo", "Henrique", "Cleiton"],
    ["Maria", "Eduarda", "José"],
    ["Claudio", "Tatiana"]
]

for index, sala in enumerate(salas):
    print(30 * "\033[36m=-=\033[m", "\033[m")
    print(f"Sala {index+1}".center(90))
    print(30 * "\033[36m=-=\033[m", "\033[m")

    for index_aluno, nome_aluno in enumerate(sala):
        print(f"{index_aluno+1}° aluno: {nome_aluno}")

print(30 * "\033[36m=-=\033[m", "\033[m")