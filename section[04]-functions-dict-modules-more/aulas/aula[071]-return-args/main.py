# permite utilizar quantos argumentos quiser
def soma(*args):
    total = 0

    for numero in args:
        total += numero

    return total


t_num = 2, 3, 4, 1, 11, 222, 2

valor = soma(2, 3, 4, 2, 5, 9, 2)
valor2 = soma(*t_num)

print(30 * "\033[36m=-=", "\033[m")
print(f"o valor da soma dos numeros é: {valor}")
print(f"o segundo valor da soma dos numeros é: {valor2}")
print(30 * "\033[36m=-=", "\033[m")