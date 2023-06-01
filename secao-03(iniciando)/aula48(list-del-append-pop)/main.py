lista1 = [123456, True, 1.15, "Valor 1"]
lista1[3] = "mudei o valor"

print(f"primeira lista: {lista1}")
print(lista1[3], type(lista1[3]))
print(30 * "-=-")

lista2 = [1, 2, 3, 4, 5, 6]

del lista2[2] # deleta o valor de uma lista

lista2.append(7)  # adiciona um valor no final da lista
lista2.append(8)

removido = lista2.pop() # deleta o ultimo valor

print(f"segunda lista: {lista2}")
print(f"valor removido: {removido}")
print(30 * "-=-")