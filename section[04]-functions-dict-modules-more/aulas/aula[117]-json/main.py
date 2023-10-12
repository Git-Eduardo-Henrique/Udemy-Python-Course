from json import dump, load
from os import getcwd

directory = f"{getcwd()}\\section[04]-functions-dict-modules-more\\aulas\\aula[117]-json\\aula[117].json"

pessoa = {
    "nome": "Eduardo",
    "idade": 18,
    "endereco" : ["rua dos bobos", 777]
}

with open(directory, "w") as arquivo:
    # dump = salva algo em um arquivo json
    dump(pessoa, arquivo)

with open(directory, "r") as arquivo:
    print(30 * "\033[31m=-=", "\033[m")
    # load = carrega informações do arquivo json
    print(load(arquivo))

    print(30 * "\033[31m=-=", "\033[m")