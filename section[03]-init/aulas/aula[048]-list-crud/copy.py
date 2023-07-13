lista1 = ["Luiz", "Among Us", 123 , -12]
lista2 = lista1
lista3 = lista1.copy()

print(30 * "=-=")
print(f"lista original: {lista1}")
print(30 * "=-=")

lista1[3] = "sus"

print(f"valor 3 mudado para: {lista1[3]}")
print(30 * "=-=")

print(f"lista copiada sem copy: {lista2}")
print(f"lista copiada com copy: {lista3}")
print(30 * "=-=")