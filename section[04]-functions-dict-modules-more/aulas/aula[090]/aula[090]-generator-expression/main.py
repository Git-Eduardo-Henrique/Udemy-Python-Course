from sys import getsizeof

lista = [num for num in range(100)]
# sabe os proximos valores porem não salva na memoria que nem uma lista
generator = (num for num in range(100))

print(30 * "\033[31m=-=", "\033[m")
print(f"tamanho da lista: \033[31m{getsizeof(lista)} bytes\033[m")
print(f"tamanho do generator: \033[31m{getsizeof(generator)} bytes\033[m")
print(30 * "\033[31m=-=", "\033[m")

for num in generator:
    print(num)

print(30 * "\033[31m=-=", "\033[m")