numero = "1"

# a variavel numero neste caso é string
print(numero, type(numero))

# a classe int() faz a conversão de certos tipos em inteiro
print(int(numero), type(int(numero)))

# a classe float() faz a conversão de certos tipos em float
print(float(numero), type(float(numero)))

# a classe bool() faz a conversão de certos tipos em boolean ( True e False )
print(bool(numero), type(bool(numero)))

# a classe str() faz a conversão de certos tipos em string
print(str(11), type(str(11)))

# caso converta false e true para int ele transforma em 0 e 1
print(int(False), int(True))