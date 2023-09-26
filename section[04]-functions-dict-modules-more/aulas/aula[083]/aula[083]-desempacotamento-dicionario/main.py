pessoa = {
    "nome": "Eduardo",
    "sobrenome": "Henrique"
}

index1, index2 = pessoa.keys() # coleta as chaves
nome, sobrenome = pessoa.values() # coleta os valores
dado1, dado2 = pessoa.items() # coleta ambos

print(30 * "\033[33m=-=", "\033[m")

print(f"dicionario = {pessoa}")
print(30 * "\033[33m=-=", "\033[m")

print(f"index1 = \033[33m{index1}\033[m\nindex2 = \033[33m{index2}\033[m")

print(30 * "\033[33m=-=", "\033[m")
print(f"nome = \033[33m{nome}\033[m\nsobrenome = \033[33m{sobrenome}\033[m")

print(30 * "\033[33m=-=", "\033[m")
print(f"dado1 = \033[33m{dado1}\033[m\ndado2 = \033[33m{dado2}\033[m")

print(30 * "\033[33m=-=", "\033[m")

novos_dados = {
    "idade": 18,
    "sexo" : "masculino"
}

pessoa_full = {
    **pessoa,
    **novos_dados
}

print(f"dicionario completo: \033[33m{pessoa_full}\033[m")
print(30 * "\033[33m=-=", "\033[m")