# cria um contador que nem o range porrem "infinito"
from itertools import count

# 10 = inicio
# 2 = passo
contador = count(10, 2)

print(30 * "\033[32m=-=", "\033[m")

for cont in contador:

    print(f"{cont}")

    if cont > 100:
        print("parando o programa para o pc não morrer")
        break

print(30 * "\033[32m=-=", "\033[m")