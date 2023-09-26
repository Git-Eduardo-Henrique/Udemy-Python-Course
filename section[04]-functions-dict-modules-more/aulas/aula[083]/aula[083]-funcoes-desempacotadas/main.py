def desempacotar(*args, **kargs):
    print(f"{args}")

    for chave, item in kargs.items():
        print(f"{chave} = {item}")


print(30 * "\033[34m=-=", "\033[m")
desempacotar(1, 2, nome='Eduardo', idade=18)
print(30 * "\033[34m=-=", "\033[m")