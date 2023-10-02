print(30 * "\033[34m=-=", "\033[m")
try:
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))

    conta = num1 / num2
    print(f"{num1} / {num2} = {conta}")

except ZeroDivisionError:
    print("\033[34mERRO: Impossivel dividir por 0\033[m")

except (TypeError, ValueError) as error:
    print(30 * "\033[34m=-=", "\033[m")

    print("\033[34mERRO: Não é possivel fazer contas com characteres\033[m")
    # melhor separar os erros do que usar isso
    print(f"MSG Do erro: \033[34m{error}\033[m")
    print(f"tipo do erro: \033[34m{error.__class__.__name__}\033[m")

print(30 * "\033[34m=-=", "\033[m")