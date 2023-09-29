def check_falsy(*values):
    for value in values:
        print(f"{value} = ", end="\033[34m")
        print("Falsy" if not value else "Thuthy", end="")
        print("\033[m")

lista = []
dicio = {}
set1 = set()
zero = 0
zerozero = 0.0
falso = False
verdade = True
numeros = range(0)

print(30 * "\033[34m=-=", "\033[m")
check_falsy(lista, dicio, set1, zero, zerozero, falso, verdade, numeros)
print(30 * "\033[34m=-=", "\033[m")