lista = [
    (x , y)
    for x in range(4)
    for y in range(4)
]

print(30 * "\033[31m=-=", "\033[m")
print("lista com mais de um for")
print(f"\033[31m{lista}\033[m")
print(30 * "\033[31m=-=", "\033[m")