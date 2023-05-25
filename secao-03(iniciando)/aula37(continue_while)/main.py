cont = 0

print(30 * "=-=")
print("iniciando contador...")
print(30 * "=-=")

while cont < 10:
    cont += 1

    if cont == 6:
        print(30 * "=-=")
        print("erro ao mostrar esse numero")
        print(30 * "=-=")
        
        continue

    print(f"contador em: {cont}")

print(30 * "=-=")
print("fim da contagem")
print(30 * "=-=")