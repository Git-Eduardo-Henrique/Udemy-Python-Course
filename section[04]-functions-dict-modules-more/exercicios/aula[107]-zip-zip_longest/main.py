from itertools import zip_longest

estados = ["Minas Gerais", "São Paulo", "Rio de Janeiro"]
estados_siglas = ["MG", "SP", "RJ", "BA", "ES"]

print(30 * "\033[32m=-=", "\033[m")
# zip = une duas listas pela menor lista
print(f"Lista Menor: \033[32m{list(zip(estados, estados_siglas))}\033[m")
# zip_longest = une duas listas pela maior lista
# fillvalue = adiciona valor caso não tenha
print(f"Lista Maior: \033[32m{list(zip_longest(estados, estados_siglas, fillvalue='SEM ESTADO'))}\033[m")
print(30 * "\033[32m=-=", "\033[m")