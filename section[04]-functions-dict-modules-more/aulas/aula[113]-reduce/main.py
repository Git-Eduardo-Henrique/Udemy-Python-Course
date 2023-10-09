from functools import reduce

prods = [
    {"nome": "mi 11", "price": 1400},
    {"nome": "mi 12", "price": 1800},
    {"nome": "mi 13", "price": 3000},
]
# lambda = função para acumular os valores do preco
# 0 = valor inicial do acumulador

total_prices = reduce(
    lambda acumulador, produto: acumulador + produto["price"],
    prods,
    0
)

print("\033[36m", 30 * "=-=", "\033[m")
print(f"produtos antigo: \033[36m{prods}\033[m\ntotal de preços: \033[36mR${total_prices}\033[m")
print("\033[36m", 30 * "=-=", "\033[m")