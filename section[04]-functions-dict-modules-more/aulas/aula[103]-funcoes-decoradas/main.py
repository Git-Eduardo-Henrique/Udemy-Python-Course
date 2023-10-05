def execute(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)

        return resultado
    
    return interna

def reverse(string):
    return string[::-1]


def is_string(value):
    if not isinstance(value, str):
        raise TypeError("\033[34mO VALOR DEVE SER STRING\033[m")

funcao = execute(reverse)

print(30 * "\033[34m=-=", "\033[m")
print(f"função: {funcao('Python')}")
print(30 * "\033[34m=-=", "\033[m")