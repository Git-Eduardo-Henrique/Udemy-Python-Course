from functools import partial

def increase_price(valor, perc):
    return round(valor * perc, 2)

# permite quarda um valor da função para usar depois
increase_ten = partial(
    increase_price,
    perc = 1.1
)

prods = [
    {"nome": "mi 11", "price": 1400},
    {"nome": "mi 12", "price": 1800},
    {"nome": "mi 13", "price": 3000},
]

new_prods = [{**p, "price": increase_ten(p["price"])} for p in prods]

list1 = [1, 2, 3, 4]

# map = usa a função em todos os items da lista1
new_list1 = list(map(
    lambda item: item * 3,
    list1
))


print("\033[34m", 30 * "=-=", "\033[m")
print(f"produtos antigo: {prods}\nprodutos novo: {new_prods}")

print("\033[34m", 30 * "=-=", "\033[m")
print(f"lista antiga: {list1}\nlista nova 3x: {new_list1}")
print("\033[34m", 30 * "=-=", "\033[m")