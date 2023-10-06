from itertools import combinations, permutations, product

def iter_print(iteravel):
    print(*list(iteravel), sep="\n")
    print(30 * "\033[33m=-=", "\033[m")

pessoas = ["Cleber", "Eduardo", "Tatiana"]

camisas = [
    ["preta", "branco"], 
    ["m", "p", "g"], 
    ["masculino", "feminino"]
]

print(30 * "\033[33m=-=", "\033[m")
# cria combinações sem repetir valores
iter_print(combinations(pessoas, 2))
# cria combinações e repete valores
iter_print(permutations(pessoas, 2))
# cria combinações usando varias listas
iter_print(product(*camisas))