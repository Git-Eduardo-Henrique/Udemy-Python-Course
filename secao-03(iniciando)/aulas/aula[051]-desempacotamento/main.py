lista = ["Python", "Udemy", "Course"]

print(30 * "\033[31m=-=\033[m", "\033[m")
print(f"lista completa: {lista}")
print(30 * "\033[31m=-=\033[m", "\033[m")

# isso irá dividir a lista em cada variavel
item1, item2, item3 = lista
print(f"item1: {item1} | item2: {item2} | item3: {item3}")

# isso irá dividir o primeiro item para a variavel item 1 e *resto para os outros items
item1, *resto = lista
print(f"item1: {item1} | resto: {resto}")

# programadores usam _ para uma variavel que não seram usados
*_, item3 = lista
print(f"item3: {item3}")

print(30 * "\033[31m=-=\033[m", "\033[m")