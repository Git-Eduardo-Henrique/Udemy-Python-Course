nome = input("digite seu nome: ")
dinheiro = float(input("quanto dinheiro voce tem? "))

# % faz o mesmo que as f strings e format so que pior
# é necessario passar o tipo da variavel com "s = string"
# %x permite passar  codigo para exadecimal
print("%s voce tem R$%.2f" % (nome, dinheiro))
print("seu dinheiro em hexadecimal é %x" % (int(dinheiro)))