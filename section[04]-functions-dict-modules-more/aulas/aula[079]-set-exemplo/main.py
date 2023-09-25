digitado = set()

print(30 * "\033[36m=-=", "\033[m")
while True:

    digito = input("digite \033[36malgo\033[m: ")
    digitado.add(str(digito).lower())

    print(f"digitados = {digitado}")
    print(30 * "\033[36m=-=", "\033[m")

    if "sair" in digitado:
        break

print("saindo...")
print(30 * "\033[36m=-=", "\033[m")