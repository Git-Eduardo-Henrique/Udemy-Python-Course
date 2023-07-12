var = "among us"
try:
    # isso não é possivel em uma variavel imbutida, como as string 
    var[3] = "sus"
except:
    print("não é possivel mudar o valor de uma casa em uma variavel imbutida")

# zfill preenche o print com 0 ate dar o numero de caracteres
print(var.zfill(20))