nome = "Eduardo Henrique"
altura = 1.77
peso = 81

imc = peso / altura ** 2

# f"" cria strings formatadas que permitem incerir valores de variaveis
linha_1 = f"{nome} voce tem {peso}kg e {altura} metros"

# :.2f faz com que o numero so tenha 2 casas depois da virgula
linha_2 = f"seu imc é de : {imc:.2f}"

print(linha_1)
print(linha_2)