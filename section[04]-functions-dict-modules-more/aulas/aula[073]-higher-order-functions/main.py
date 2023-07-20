def bomdia(texto, nome):
    return f"{texto} {nome}!"

def executar(func, texto, nome):
    return func(texto, nome)


print(30 * "\033[32m=-=", "\033[m")
print(executar(bomdia, "Olá senhor(a)", "Eduardo"))
print(30 * "\033[32m=-=", "\033[m")