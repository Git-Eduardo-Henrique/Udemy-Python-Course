senha = "segredo"

letras_acertadas = ""
tentativas = 0

while True:
    letra_digitada = input("digite uma letra: ")
    tam_letra = len(letra_digitada)

    if tam_letra > 1:
        print("digite APENAS uma letra!!!!")
        continue

    if letra_digitada in senha:
        letras_acertadas += letra_digitada

    import os
    
    nova_palavra = ""
    for letras_senha in senha:
        if letras_senha in letras_acertadas:
            nova_palavra += letras_senha
        else:
            nova_palavra += "*"

    print(f"senha: {nova_palavra}")

    tentativas += 1

    if nova_palavra == senha:
        os.system("cls") # limpa o terminal

        print(f"senha: {senha}")
        print("você acertou a senha!!!")
        print(f"tentativas = {tentativas}")
        break