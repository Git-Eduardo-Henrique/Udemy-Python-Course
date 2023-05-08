print("=-=" * 30)
nome = str(input("Digite seu nome: "))
idade = input("Digite sua idade: ")
print("=-=" * 30)
# string sem nada = false
if nome and idade:
    print(f"seu nome: {nome}")
    print(f"seu nome invertido: {nome[::-1]}")

    if " " in nome:
        print(f"seu nome tem espaços!")
    else:
        print(f"seu nome não tem espaços")

    print(f"primeira letra do nome: {nome[0]}")
    print(f"ultima letra do nome: {nome[-1]}")
else:
    print("preencha todos os campos")

print("=-=" * 30)