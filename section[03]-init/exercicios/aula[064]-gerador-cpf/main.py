from random import randint

dois_digitos = []
soma1 = soma2 = 0
cpf = ""

for _ in range(9):
    cpf += str(randint(0, 9))

# validadando digito 1 
index = 0
for cont in range(10, 1, -1):
    soma1 += (int(cpf[index]) * (cont))
    index += 1

soma1 = soma1 * 10 % 11

if soma1 > 9:
    soma1 = 0
    dois_digitos.append(soma1)
else:
    dois_digitos.append(soma1)

# validadando digito 2
cpf += str(dois_digitos[0])

index = 0
for cont in range(11, 1, -1):
    soma2 += (int(cpf[index])  * cont)
    index += 1

soma2 = soma2 * 10 % 11

if soma2 > 9:
    soma2 = 0
    dois_digitos.append(soma2)
else:
    dois_digitos.append(soma2)

# para adicionar os . e -
cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{dois_digitos[0]}{dois_digitos[1]}"

print(30 * "\033[34m=-=\033[m", "\033[m")
print(f"cpf gerado: {cpf}")
print(30 * "\033[34m=-=\033[m", "\033[m")