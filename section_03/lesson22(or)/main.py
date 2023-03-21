print("=" * 50)
print("Cofre de segurança maxima (confia)")

print("=" * 50)
entrar = input("[e] para entrar: ")
print("=" * 50)
# or executa o codigo caso alguma condição for verdadeira
if entrar == "E" or entrar == "e":

    senha_entrada1 = input("primeira senha: ")
    senha_entrada2 = input("segunda senha: ")
    print("=" * 50)

    senha1 = "sus"
    senha2 = "amongus"

    # and valida duas condições e se as duas forem verdadeiras ele executa o codigo
    if senha_entrada1 == senha1 and senha_entrada2 == senha2:
        print("pou 2 foi desbloqueado!!!!")
    else:
        print("acesso negado")
else:
    print("que pena")

print("=" * 50)