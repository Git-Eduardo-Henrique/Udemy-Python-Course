produto = [
    ("nome", "Pc gamer"),
    ("preco", 2000),
    ("categoria", "computadores")
]

dc = {
    # cria a chave e o valor do dicionario
    chave: valor.upper()
    # isinstace = checa se o valor é um str
    # se não for ele rotornara o valor sem usar o upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto
}

print(30 * "\033[32m=-=", "\033[m")
print(dc)
print(30 * "\033[32m=-=", "\033[m")