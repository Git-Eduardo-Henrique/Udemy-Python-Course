perguntas = [
    {
        "pergunta" : "Quanto é 2 x 8 - 12",
        "opcoes" : [3, 8, 4, -4],
        "resposta" : 4
    },
    {
        "pergunta" : "Quanto é 40 / 20",
        "opcoes" : [2, 20, 10, 4],
        "resposta" : 2
    },
    {
        "pergunta" : "Quanto é (2 + 2) x (4 - 2)",
        "opcoes" : [4, 8, -4, 2],
        "resposta" : 8
    }
]

acertou = 0

for dicionario in perguntas:
    opc = " "
    print(30 * "\033[35m=-=", "\033[m")
    print(f"pergunta: {dicionario['pergunta']}")
    print(30 * "\033[35m=-=", "\033[m")

    for key, item in enumerate(dicionario['opcoes']):
        print(f"{key+1}) {item}")

    print(30 * "\033[35m=-=", "\033[m")
    opc = int(input("sua opção: "))

    if dicionario["opcoes"][opc-1] == dicionario["resposta"]:
        print("acertou")
        acertou += 1
    else:
        print("errou")

print(30 * "\033[35m=-=", "\033[m")
print(f"você acertou {acertou} perguntas")
print(30 * "\033[35m=-=", "\033[m")