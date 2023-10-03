try:
    print(30 * "\033[35m=-=", "\033[m")
    num1 = int(input("digite o primeiro numero: "))
    num2 = int(input("digite o segundo numero: "))

    conta = num1 / num2

    print(30 * "\033[35m=-=", "\033[m")
    print(f"{num1} / {num2} = {conta}")
    print(30 * "\033[35m=-=", "\033[m")

except ZeroDivisionError:
    print(30 * "\033[35m=-=", "\033[m")
    print("\033[35mERRO: Impossivel dividir por 0\033[m")

except (TypeError, ValueError) as error:
    print(30 * "\033[35m=-=", "\033[m")
    print("\033[35mERRO: Não é possivel fazer contas com characteres\033[m")

# executa se não ouver erros
else:
    print("\033[35mNão ocorreu erro! :)\033[m")

# executa sempre 
finally:
    print(30 * "\033[35m=-=", "\033[m")
    print("Encerrando...")
    print(30 * "\033[35m=-=", "\033[m")