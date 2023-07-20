def saudacao(texto = "Olá"):
    
    def saudar(nome = "Desconhecido(a)"):
        return f"{texto}, {nome}"
    
    # IRÁ SALVAR O TEXTO NA VARIAVEL E SO EXECUTAR QUANDO ESCREVER ()
    return saudar


dia = saudacao("Bom dia senhor(a)")
noite = saudacao("Boa noite senhor(a)")

print(30 * "\033[33m=-=", "\033[m")
print(f"{dia('Eduardo')}\n{noite()}")
print(30 * "\033[33m=-=", "\033[m")