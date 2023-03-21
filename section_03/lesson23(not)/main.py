print("=" * 50)
print("Cofre de segurança maxima (confia)")

print("=" * 50)
entrar = input("[e] para entrar: ")
print("=" * 50)

if entrar == "E" or entrar == "e":

    senha_entrada1 = input("primeira senha: ")
    senha_entrada2 = input("segunda senha: ")
    print("=" * 50)

    senha1 = "sus"
    senha2 = "amongus"

    # not valida se algo é falso como por exemplo string vazia
    if not senha_entrada1 or not senha_entrada2:
        print("voce não digitou algo!!!")
    else:
        if senha_entrada1 == senha1 and senha_entrada2 == senha2:
            print("pou 2 foi desbloqueado!!!!")
        else:
            print("acesso negado")

else:
    print("que pena")

print("=" * 50)