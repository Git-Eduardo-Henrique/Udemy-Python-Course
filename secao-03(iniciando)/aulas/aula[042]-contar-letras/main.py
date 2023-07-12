frase = input("escreva algo: ")
cont = 0
maior_letra = ' '

while cont < len(frase):
    letra = frase[cont]

    cont += 1

    if letra == " ":
        continue

    if frase.count(letra) > frase.count(maior_letra):
        maior_letra = letra

print(f"a letra que apareceu mais foi: '{maior_letra}' ela apareceu {frase.count(maior_letra)} vezes")