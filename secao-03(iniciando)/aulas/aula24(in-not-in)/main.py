entrada = input("digite algo: ")
checar = input("digite algo para verificar a primeira palavra: ")
print(15 * "=-=")

# in verifica se algum valor esta em outro valor
if checar in entrada:
    print(f"{checar} está em {entrada}")
else:
    print(f"{checar} não está em {entrada}")

print(15 * "=-=")
print("agora tente colocar uma letra que está na palavra secreta!")
entrada2 = input("digite algo: ")
palavra_secreta = "sus"

# not in verifica se algum valor não esta em outro valor
if entrada2 not in palavra_secreta:
    print(f"{entrada2} não está em na palavra secreta :(")
else:
    print(f"{entrada2} está em {palavra_secreta}")