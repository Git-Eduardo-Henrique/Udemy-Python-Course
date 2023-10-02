
def gerador(n=0, max=10):
    while True:
        # pausa a função e retorna "n"
        yield n
        n += 1

        if n > max:
            return "Acabou wow"

gen = gerador()

print(30 * "\033[32m=-=", "\033[m")

for n in gen:
    print(n)

print(30 * "\033[32m=-=", "\033[m")