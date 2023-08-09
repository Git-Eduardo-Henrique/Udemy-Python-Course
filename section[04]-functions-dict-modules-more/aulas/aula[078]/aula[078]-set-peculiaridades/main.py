set1 = set()
set2 = {1, 2, 3, 4}
set3 = {1, 1, 2, 2, 4, 3, 3}

print(30 * "\033[33m=-=", "\033[m")
print(f"o set: {set1} | {type(set1)}")
print(f"set com valores: {set2} | {type(set2)}")
# set não pode ter valores iguais
print(f"set com 'varios' valores: {set3} | {type(set3)}")
print(30 * "\033[33m=-=", "\033[m")

# lista para set
lista = [1, 2, 3, 5, 5, 6]
print(f"lista: {lista} | {type(lista)}")

set4 = set(lista)
lista = list(set4)
print(f"nova lista: {lista}")

print(30 * "\033[33m=-=", "\033[m")