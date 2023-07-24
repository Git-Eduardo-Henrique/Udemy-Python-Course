# ---- Create

# pessoa = dict()
pessoa = {
    "nome": "Cleber",
    "sobrenome": "Henrique",
    "idade": 18,
}

# ---- Update
pessoa["nome"] = "Eduardo"

# ---- Delete
del pessoa["sobrenome"]

# ---- Checar chave
# retorna None se não encontrar a chave
if pessoa.get("sobrenome") is None:
    print(30 * "\033[35m=-=", "\033[m")
    print("Sobrenome não foi encontrado no dicionário")

# ---- Read
print(30 * "\033[35m=-=", "\033[m")

for key in pessoa:
    print(f"{key} = {pessoa[key]}")

print(30 * "\033[35m=-=", "\033[m")