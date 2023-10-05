def execute(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)

        resultado = func(*args, **kwargs)

        return resultado
    
    return interna

# @ - executa a função automaticamente e manda a funcao "reverse" no "func"
@execute
def reverse(string):
    return string[::-1]


def is_string(value):
    if not isinstance(value, str):
        raise TypeError("\033[35mO VALOR DEVE SER STRING\033[m")

funcao = reverse("Python")

print(30 * "\033[35m=-=", "\033[m")
print(f"função: {funcao}")
print(30 * "\033[35m=-=", "\033[m")