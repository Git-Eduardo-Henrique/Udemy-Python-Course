nome = input("digite seu nome: ")
print(30 * "=-=")
print("separando seu nome em letras...")
print(30 * "=-=")

cont = 0
while cont < len(nome):
    cont += 1
    print(f"{cont} letra: {nome[cont - 1]}")

print(30 * "=-=")