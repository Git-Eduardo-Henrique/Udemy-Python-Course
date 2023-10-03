def verificar_numero(num):
    if not isinstance(num, (float, int)):
        # torna possivel criar erros
        raise TypeError(f"\033[36m{num} não é um numero inteiro ou decimal e sim {type(num)}\033[m")

def verificar_zero(n, d):
    if d == 0:
        # torna possivel criar erros
        raise ZeroDivisionError(f"\033[36mImpossivel dividir {n} por 0\033[m")

def dividir_dois(n=0, d=1):
    verificar_zero(n, d)
    verificar_numero(n)
    verificar_numero(d)

    divi = n / d
    return f"{n} / {d} = {divi}"

print(30 * "\033[36m=-=", "\033[m")
print(dividir_dois(10, 2))
print(dividir_dois(10, 0))
print(30 * "\033[36m=-=", "\033[m")