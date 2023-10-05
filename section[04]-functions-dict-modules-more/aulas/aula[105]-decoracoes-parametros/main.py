def create_decorator(a=None, b=None, c=None):
    def create_function(function):

        def aninhada(*args, **kwargs):
            print(f"parametros do decorador: {a}, {b}, {c}")
            res = function(*args, **kwargs)
            return res
        return aninhada
    
    return create_function

@create_decorator(1, 2, 3)
def soma(n1, n2):
    return n1 + n2

print(30 * "\033[36m=-=", "\033[m")
print(f"soma: {soma(12, 22)}")
print(30 * "\033[36m=-=", "\033[m")