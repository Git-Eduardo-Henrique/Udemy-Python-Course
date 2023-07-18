# criar função
# x - y = parametros
# z = | para dar valores padrão
def soma(x, y, z = None):
    if z is None:
        print(f"{x} + {y} = {x + y}")
    else:
        print(f"{x} + {y} + {z} = {x + y + z}")

print(30 * "\033[33m=-=", "\033[m")
soma(9, 5)
soma(x=92, y=212)
soma(y=3, x=112, z=22)
print(30 * "\033[33m=-=", "\033[m")