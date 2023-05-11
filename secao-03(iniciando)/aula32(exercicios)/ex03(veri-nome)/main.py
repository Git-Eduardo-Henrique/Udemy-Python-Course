print(20 * "=-=")
nome = input("digite seu nome: ")
n_tam = len(nome)
print(20 * "=-=")
print(nome)
print(20 * "=-=")

if n_tam <= 4:
    print(f"seu nome é pequeno e tem {n_tam} letras")
elif n_tam <= 6:
    print(f"seu nome é normal e tem {n_tam} letras")
else:
    print(f"seu nome é grande e tem {n_tam} letras")

print(20 * "=-=")