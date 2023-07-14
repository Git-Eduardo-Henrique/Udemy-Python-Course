# 746.824.890-70
# 984.264.930-09
nove_digitos = []
dois_digitos = []
soma = 0

print(30 * "\033[32m=-=\033[m", "\033[m")
cpf = str(input("digite um cpf (ex: 222.222.222-22): "))
print(30 * "\033[32m=-=\033[m", "\033[m")

for index, digito in enumerate(cpf):
    if index <= 10:
        if digito != "." and digito.isnumeric():
            nove_digitos.append(int(digito))
       
    else:
        if digito != "-" and len(dois_digitos) < 2 and digito.isnumeric():
            dois_digitos.append(int(digito))


index = 0
for cont in range(10, 1, -1):
    soma += (nove_digitos[index] * cont)
    index += 1

soma *= 10
soma %= 11

if soma > 9:
    soma = 0

print(f"cpf: {cpf} \nnove digitos: {nove_digitos}\ndois digitos finais: {dois_digitos}\nprimeiro digito: {soma}")

if soma == dois_digitos[0]:
    print("primeiro digito valido!")
else:
    print("primeiro digito invalido! esse cpf não existe")

print(30 * "\033[32m=-=\033[m", "\033[m")