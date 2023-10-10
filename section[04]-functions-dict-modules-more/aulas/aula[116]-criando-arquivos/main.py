from os import getcwd

directory = getcwd()

directory = f"{directory}\\section[04]-functions-dict-modules-more\\aulas\\aula[116]-criando-arquivos\\aula[116].txt"

# open = abrir arquivo
# w = caso não haja ele irá criar

# with usa o arquivo e fecha o arquivo no final
with open(directory, "w") as arquivo:
    print("\033[32m", 30 * "=-=", "\033[m")
    print(directory)
    print("\033[32m", 30 * "=-=", "\033[m")
