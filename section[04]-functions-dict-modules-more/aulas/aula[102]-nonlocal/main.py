def concatenar(inicial=""):
    valor_final = inicial

    def interna(final):
        # permite utilizar variaveis que não estão nesta função
        nonlocal valor_final

        valor_final += final
        return valor_final
    
    return interna

python = concatenar("python")

print(30 * "\033[33m=-=", "\033[m")

print(f"\033[33m{python(' é muito bom')}\033[m")

print(30 * "\033[33m=-=", "\033[m")