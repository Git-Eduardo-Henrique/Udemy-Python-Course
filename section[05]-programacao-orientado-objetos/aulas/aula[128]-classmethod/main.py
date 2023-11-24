class Pessoas():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # transforma o self, na propria classe em sí
    @classmethod
    def criar_sem_nome(cls, idade):
        # cls = classe Pessoas
        return cls("Anônima", idade)

pessoa1 = Pessoas("Eduardo", 18)
pessoa2 = Pessoas.criar_sem_nome(20)

print("\033[34m", 30 * "=-=", "\033[m")

print(f"Pessoa 1 \nnome = {pessoa1.nome} | idade = {pessoa1.idade}")
print("\033[34m", 30 * "=-=", "\033[m")
print(f"Pessoa 2 \nnome = {pessoa2.nome} | idade = {pessoa2.idade}")

print("\033[34m", 30 * "=-=", "\033[m")