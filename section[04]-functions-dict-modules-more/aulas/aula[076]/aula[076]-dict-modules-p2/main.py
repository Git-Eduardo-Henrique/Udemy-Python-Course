pessoa = {
    "nome" : "Eduardo",
    "sobrenome" : "Henrique",
    "local" : "Rua muito top 174"
}

print(30 * "\033[32m=-=", "\033[m")

# acha o valor e se não tiver retorna o segundo | normal: none
print(f"nome: {pessoa.get('nome')}\nidade: {pessoa.get('idade', 'não tem')}")
# pop() remove um valor de um dicionario e o guarda
print(f"valor removido: {pessoa.pop('sobrenome')}")
# popitem() remove o ultimo valor
print(f"ultimo valor removido: {pessoa.popitem()}")
# update() permite atualizar a lista, adicionando e modificando
pessoa.update(
    {
        "nome" : "Eduardo Henrique",
        "idade" : 18
    }
)
print(f"dicionario atualizado: {pessoa}")

print(30 * "\033[32m=-=", "\033[m")