prods = [
    {"nome": "mi 11", "price": 1400},
    {"nome": "mi 12", "price": 1800},
    {"nome": "mi 13", "price": 3000},
]

# filtra pelo parametro, ex: < 2000
new_prods = list(filter(lambda prod : prod["price"] < 2000, prods))

print("\033[35m", 30 * "=-=", "\033[m")
print(f"produtos antigo: \033[35m{prods}\033[m\nprodutos novo: \033[35m{new_prods}\033[m")
print("\033[35m", 30 * "=-=", "\033[m")