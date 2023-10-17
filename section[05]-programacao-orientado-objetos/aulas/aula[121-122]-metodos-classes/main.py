class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def acelerar(self):
        print(f"o carro \033[35m{self.nome}\033[m da marca \033[35m{self.marca}\033[m está acelerando")

fusca = Carro(nome="Fusca", marca="Volkswagen")
celta = Carro(nome="Celta", marca="Chevrolet")

print(30 * "\033[35m=-=", "\033[m")
fusca.acelerar()
celta.acelerar()
print(30 * "\033[35m=-=", "\033[m")