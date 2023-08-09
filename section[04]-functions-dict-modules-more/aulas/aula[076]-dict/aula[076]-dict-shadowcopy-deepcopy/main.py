from copy import deepcopy

pessoa1 = {
    "nome" : "Eduardo",
    "sobrenome" : "Henrique",
    "l1" : [1, 2, 3]
}
# cria um dicionario e lista igual
pessoa3 = deepcopy(pessoa1)
pessoa3["l1"][1] = 2222

# o copy cria um dicionario igual, porem a lista ainda aponta para o mesmo local da memoria
pessoa2 = pessoa1.copy()
pessoa2["l1"][1] = 99999

print(30 * "\033[31m=-=", "\033[m")

print(f"{pessoa1}\n{pessoa2}\n{pessoa3}")

print(30 * "\033[31m=-=", "\033[m")