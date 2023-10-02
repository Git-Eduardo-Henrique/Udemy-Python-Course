def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    # retorna informações de outro lugar
    yield from gen1()
    yield 4
    yield 5
    yield 6

gen = gen2()

print(30 * "\033[33m=-=", "\033[m")

for numero in gen:
    print(numero)

print(30 * "\033[33m=-=", "\033[m")