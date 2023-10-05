def create_decorator(a=None, b=None, c=None):
    def create_function(function):

        def aninhada(*args, **kwargs):
            print(f"parametros do decorador: {a}, {b}, {c}")
            res = function(*args, **kwargs)
            return res
        return aninhada
    
    return create_function

# decoradores executão de cima para baixo
@create_decorator(1, 2, 3)
@create_decorator(4, 5, 6)
@create_decorator(7, 8, 9)
def soma(n1, n2):
    return n1 + n2

print(30 * "\033[31m=-=", "\033[m")
print(f"soma: {soma(12, 22)}")
print(30 * "\033[31m=-=", "\033[m")