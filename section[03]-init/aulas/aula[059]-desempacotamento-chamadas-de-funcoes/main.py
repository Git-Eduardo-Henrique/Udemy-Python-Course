salas = [
    ["Eduardo", "Henrique", "Cleiton"],
    ["Maria", "Eduarda", "José"],
    ["Claudio", "Tatiana"]
]

print(30 * "\033[31m=-=\033[m", "\033[m")
print(*salas, end="\n")
print(30 * "\033[31m=-=\033[m", "\033[m")