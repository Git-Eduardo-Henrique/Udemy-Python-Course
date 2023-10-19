from package import save_json, load_json

class Pessoa:

    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

pessoas = load_json()

print("\033[34m", 30 * "=-=", "\033[m")
nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
print("\033[34m", 30 * "=-=", "\033[m")

pessoa = Pessoa(nome, idade)
pessoas.append(vars(pessoa))

save_json(pessoas)
print("\033[34m", 30 * "=-=", "\033[m")