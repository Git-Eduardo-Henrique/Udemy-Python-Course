listas = [
    [1, 2, 3, 5, 4, 2, 1],
    [2, 3, 4, 10, 3, 10, 2],
    [9, 8, 7, 3, 1, 9, 7],
    [4, 5, 6, 10, 4, 10, 6],
    [1, 2, 3, 4, 5, 6, 7]
]

def encontra_dupli(lista = []):
    numeros = set()
    duplicado = -1

    for numero in lista:
        if numero in numeros:
            duplicado = numero
            break

        numeros.add(numero)

    return duplicado

for lista in listas:
    print(30 * "\033[36m=-=", "\033[m")
    print(f"lista: \033[36m{lista}\033[m")
    print(f"primeiro numero duplicado ( -1 = não possui ): \033[36m{encontra_dupli(lista=lista)}\033[m")

print(30 * "\033[36m=-=", "\033[m")