lista = ["Eduardo", "Henrique", "Among Us", 123, True]

indices = range(len(lista))

print(30 * "=-=")

for indice in indices:
    item = lista[indice]
    print(f"item N°{indice}: {item} | tipo: {type(item)}")

print(30 * "=-=")
