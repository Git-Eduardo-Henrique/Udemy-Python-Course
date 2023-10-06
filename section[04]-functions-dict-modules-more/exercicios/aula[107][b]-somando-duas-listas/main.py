list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 2, 3, 4]

new_full_list = []

for item1, item2 in zip(list1, list2):
    new_full_list.append(item1 + item2)

print(30 * "\033[33m=-=", "\033[m")
print(f"listas originais: \033[33m{list1} | {list2}\033[m")
print(f"lista somada: \033[33m{new_full_list}\033[m")
print(30 * "\033[33m=-=", "\033[m")