def somar(n1, n2):
    return n1 + n2

def multi(n1, n2):
    return n1 * n2

def execute(func, n1):
    def salvar(n2):
        return func(n1, n2)
    
    return salvar

print(30 * "\033[32m=-=", "\033[m")

somar_com_cinco = execute(somar, 5)
multiplica_com_dez = execute(multi, 10)

print(f"\033[32m{somar_com_cinco(10)}\033[m")
print(f"\033[32m{multiplica_com_dez(10)}\033[m")

print(30 * "\033[32m=-=", "\033[m")