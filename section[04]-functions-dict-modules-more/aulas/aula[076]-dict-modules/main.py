pessoa = {
    "nome" : "Eduardo",
    "sobrenome" : "Henrique"
}

print(30 * "\033[36m=-=", "\033[m")

# retorna chave e valor do dicionario
print(f"items do dicionario: {list(pessoa.items())}")
# retorna chaves de um dicionario
print(f"chaves do dicionairo: {list(pessoa.keys())}")
# retorna valores de um dicionario
print(f"valores do dicionarios: {list(pessoa.values())}")
# se não ouver idade ele irá seletar o valor padrão
pessoa.setdefault("idade", 18)
print(f"idade: {pessoa['idade']}")

print(f"tamanho do dicionario: {len(pessoa)}")

print(30 * "\033[36m=-=", "\033[m")