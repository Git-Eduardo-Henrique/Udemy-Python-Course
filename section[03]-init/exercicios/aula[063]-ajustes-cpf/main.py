from re import sub

# 746.824.890-70
dois_digitos = []
soma1 = soma2 = 0
cpf_gerado = checar_cpf_igual = ""

print(30 * "\033[34m=-=\033[m", "\033[m")
cpf = str(input("digite um cpf (ex: 222.222.222-22): "))

# usado para formatar
cpf = sub(r'[^0-9]', "", cpf)

# para checar se todos os digitos são iguais
checar_cpf_igual = cpf[0] * len(cpf)

print(30 * "\033[34m=-=\033[m", "\033[m")

if len(cpf) != 11:
    print("\033[31mCPF LONGO OU CURTO DEMAIS!!!\033[m")
elif cpf == checar_cpf_igual:
    print("\033[31mDIGITOS DO CPF NÃO PODEM SER TODOS IGUAIS\033[m")
else:
    # validadando digito 1 e 2
    index = 0
    for cont in range(11, 1, -1):
    
        if cont > 2:  # para validar o primeiro digito
            soma1 += (int(cpf[index]) * (cont - 1))

        soma2 += (int(cpf[index])  * cont)
        index += 1

    soma1 = soma1 * 10 % 11
    soma2 = soma2 * 10 % 11

    if soma1 > 9:
        soma1 = 0
        dois_digitos.append(soma1)
    else:
        dois_digitos.append(soma1)

    if soma2 > 9:
        soma2 = 0
        dois_digitos.append(soma2)
    else:
        dois_digitos.append(soma2)

    # para adicionar os . e -
    cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    cpf_gerado = f"{cpf[:11]}-{dois_digitos[0]}{dois_digitos[1]}"


    print(f"cpf digitado: {cpf} \ncpf gerado: {cpf_gerado}")
    print(30 * "\033[34m=-=\033[m", "\033[m")

    if cpf == cpf_gerado:
        print("CPF VALIDADO!!")
    else:
        print("\033[31mCPF INVALIDO!!!\033[m")

print(30 * "\033[34m=-=\033[m", "\033[m")