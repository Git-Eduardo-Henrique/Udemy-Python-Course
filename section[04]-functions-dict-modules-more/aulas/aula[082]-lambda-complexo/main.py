def executar(func, *args):
    return func(*args)


print(30 * "\033[32m=-=", "\033[m")

# função de soma com lambda
print(f"24 + 102 = {executar(lambda x, y: x + y, 24, 102)}")

# função de multiplicar com lambda
duplica = executar(lambda m: lambda n: n * m, 102)
print(f"24 x 102 = {duplica(24)}")

# função de soma com varios parametros em lambda
print(f"1 + 2 + 3 + 4 + 5 = {executar(lambda *args: sum(args), 1, 2, 3, 4, 5)}")

print(30 * "\033[32m=-=", "\033[m")