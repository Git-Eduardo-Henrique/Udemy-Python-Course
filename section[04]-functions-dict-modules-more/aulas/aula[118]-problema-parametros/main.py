# fazendo isso o python íra reutilizar a lista caso não seja passada

# def adicionar(nome, lista=[]):
#     lista.append(nome)
#     return lista

def adicionar(nome, lista=None):

    if lista is None:
        lista = []

    lista.append(nome)
    return lista

lista1 = adicionar("Julio") 
adicionar("Eduardo", lista1)
lista2 = adicionar("Marcos")
adicionar("Pedro", lista2)

print(30 * "\033[32m=-=", "\033[m")
print(f"lista 1: \033[32m{lista1}\033[m\nlista 2: \033[32m{lista2}\033[m")
print(30 * "\033[32m=-=", "\033[m")