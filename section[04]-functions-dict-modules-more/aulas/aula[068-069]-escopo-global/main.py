valor = 1

def func1():
    valor = 11
    print(f"o valor da funcao 1: {valor}")

def func2():
    # assim ele irá utilizar a variavel valor do escopo global
    global valor
    valor = 12
    print(f"utilizando o valor normal na função 2: {valor}")

print(30 * "\033[34m=-=", "\033[m")

print(f"valor normal: {valor}")
func1()
func2()

print(30 * "\033[34m=-=", "\033[m")