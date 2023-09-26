precos = [
    {"nome": "xiaomi mi11", "preco": 1500},
    {"nome": "achocolatado", "preco": 8},
    {"nome": "ventilador 6 pas", "preco": 110}
]

novos_precos = [
    {**produto, "preco": produto["preco"] * 1.05}
    for produto in precos
]

print(30 * "\033[36m=-=", "\033[m")
print(f"{novos_precos}")
print(30 * "\033[36m=-=", "\033[m")