from datetime import datetime

class Pessoa:
    # para usar essa variavel devesse fazer assim: Pessoa.ano
    ano = datetime.now()
    ano = ano.year

    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade

    def mostrar_ano_nascimento(self):
        return Pessoa.ano - self.idade

# Pessoa.ano = 1 iria mudar para todas as pessoas

eduardo = Pessoa("Eduardo", 19)
theo = Pessoa("Theo", 9)

print("\033[32m", 30 * "=-=", "\033[m")
print(f"ano atual: {Pessoa.ano}")
print(f"{eduardo.nome} tem {eduardo.idade} anos e nasceu em {eduardo.mostrar_ano_nascimento()}")
print(f"{theo.nome} tem {theo.idade} anos e nasceu em {theo.mostrar_ano_nascimento()}")
print("\033[32m", 30 * "=-=", "\033[m")