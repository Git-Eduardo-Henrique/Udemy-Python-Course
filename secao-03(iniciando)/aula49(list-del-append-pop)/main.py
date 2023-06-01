lista = [1, 2, 3, 4, 5, 6]

del lista[2] # deleta o valor de uma lista

lista.append(7)  # adiciona um valor no final da lista
lista.append(8)

removido = lista.pop() # deleta o ultimo valor

print(lista)
print(f"valor removido: {removido}")