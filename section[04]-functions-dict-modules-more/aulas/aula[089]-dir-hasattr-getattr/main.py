string = "Frase Top"

print(30 * "\033[35m=-=", "\033[m")
print(f"{f'Todos os metodos desta string: {string}':^90}")
print(30 * "\033[35m=-=", "\033[m")

# mostra todos os metodos disponiveis na string
print(dir(string))

print(30 * "\033[35m=-=", "\033[m")

metodo = str(input(f"qual metodo você deseja usar em '{string}': "))

# "hasattr" checa se o metodo existe na string, ex: upper, lower, etc...
if hasattr(string, metodo):
    print(f"o metodo \033[35m{metodo}\033[m existe em \033[35m'{string}'\033[m")
    # usa o metodo em uma variavel
    print(f"\033[35m{getattr(string, metodo)()}\033[m")

else:
    print(f"o metodo \033[35m{metodo}\033[m não existe em \033[35m'{string}'\033[m")

print(30 * "\033[35m=-=", "\033[m")