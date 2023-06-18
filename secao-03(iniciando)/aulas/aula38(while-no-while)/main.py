print(30 * "=-=")

num_linhas = 5
num_colunas = 5

linha = 1
while linha < num_linhas:
    coluna = 1

    while coluna <= num_colunas:
        print(f"{linha=}, {coluna=}")
        coluna += 1

    linha += 1
