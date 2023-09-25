pessoas = [
    {"nome": "Eduardo", "sobrenome": "Henrique"},
    {"nome": "Matheus", "sobrenome": "Felipe"},
    {"nome": "Ana", "sobrenome": "Maria"},
    {"nome": "Paulo", "sobrenome": "Henrique"}
]

def exibir(lista):
    for item in lista:
        print(item)

l_nome = sorted(pessoas, key=lambda item: item["nome"])
l_sobrenome = sorted(pessoas, key=lambda item: item["sobrenome"])

print(30 * "\033[31m=-=", "\033[m")
exibir(l_nome)
print(30 * "\033[31m=-=", "\033[m")
exibir(l_sobrenome)
print(30 * "\033[31m=-=", "\033[m")