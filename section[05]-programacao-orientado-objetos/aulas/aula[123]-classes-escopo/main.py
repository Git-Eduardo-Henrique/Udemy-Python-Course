class Animal:
    def __init__(self, nome=""):
        self.nome = nome

        variavel = "teste"
        print(f"está variavel não pode ser usada fora do escopo: {variavel}")

    def comer(self, comida="carne"):
        return f"\033[36m{self.nome}\033[m está comendo \033[36m{comida}\033[m"

leao = Animal(nome="Leão")
cachorro = Animal(nome="Cachorro")

print(30 * "\033[36m=-=", "\033[m")
print(leao.comer(comida="picanha"))
print(cachorro.comer(comida="ração"))
print(30 * "\033[36m=-=", "\033[m")