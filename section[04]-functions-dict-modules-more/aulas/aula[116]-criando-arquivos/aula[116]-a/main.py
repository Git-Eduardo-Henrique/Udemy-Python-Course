from os import getcwd

directory = getcwd()

directory = f"{directory}\\section[04]-functions-dict-modules-more\\aulas\\aula[116]-criando-arquivos\\aula[116].txt"

# a = escreve sem apagar o texto do arquivo
with open(directory, "a") as arquivo:

    arquivo.write("Linha 1\n")
    arquivo.writelines(("Linha 2\n", "Linha 3\n", "Linha 4\n"))

with open(directory, "r") as arquivo:
    print("\033[32m", 30 * "=-=", "\033[m")
    # read = le as linhas do arquivo
    print(arquivo.read())
    print("\033[32m", 30 * "=-=", "\033[m")