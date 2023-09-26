# deve ser colocado o retorno antes do "for"
lista_num = [numero for numero in range(10)]

lista_dobro = [numero * 2 for numero in range(10)]

print(30 * "\033[35m=-=", "\033[m")
print(f"lista de numeros: \033[35m{lista_num}\033[m")
print(f"lista de numeros vezes 2: \033[35m{lista_dobro}\033[m")
print(30 * "\033[35m=-=", "\033[m")