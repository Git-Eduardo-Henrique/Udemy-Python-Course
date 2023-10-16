class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

pessoa1 = Pessoa("Eduardo", "Henrique")
pessoa2 = Pessoa("Theo", "Marcos")

print(30 * "\033[34m=-=", "\033[m")
print(f"pessoa 1: {pessoa1.nome} {pessoa1.sobrenome}\npessoa 2: {pessoa2.nome} {pessoa2.sobrenome}")
print(30 * "\033[34m=-=", "\033[m")