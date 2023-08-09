# create
set1 = set()
set1.add("sus")

# read
print(30 * "\033[34m=-=", "\033[m")
print(f"set: {set1}")
print(30 * "\033[34m=-=", "\033[m")

# update
# adiciona: "u", "s"
set1.update("sus")
# adiciona: 1, 2, 3
set1.update(("sus", 1, 2, 3))

# delete
set1.discard("sus")
print(f"set com sus removido: {set1}")
set1.clear()
print(f"set completamente vazio: {set1}")

print(30 * "\033[34m=-=", "\033[m")