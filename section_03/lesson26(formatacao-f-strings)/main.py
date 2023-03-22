nome = input("digite seu nome: ")
dinheiro = float(input("quanto dinheiro voce tem? "))
print(15 * "=-=")

print(f"{nome} voce tem R${dinheiro:.2f}")
print(15 * "=-=")
# > faz a variavel preencher um numero de casas e ir para a direita
# < faz a variavel preencher um numero de casas e ir para a esquerda
# ^ faz a variavel preencher um numero de casas e ficar centralizado
print(f"{dinheiro: > 10}")
print(f"{dinheiro: < 10}")
print(f"{dinheiro: ^ 10} ")
print(15 * "=-=")
# mostra o codigo exadecimal de um numero
print(f"seu dinheiro em hexadecimal: {int(dinheiro):x}")
print(15 * "=-=")