print(30 * "=-=")
print("calculadora com while")
print(30 * "=-=")

opc_list = ("+", "-", "*", "/")
calc = float
num1 = float
num2 = float

while True:
        # retorna um valor boolean se começar com a letra escolhida
        sair = input("você deseja continuar? (n = não): ").lower().startswith("n")
        print(30 * "=-=")

        if sair:
            break

        try:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero: "))
        except Exception as error:
            print(30 * "=-=")
            print(f"valor invalido!!!!! | Error: {error}")
            print(30 * "=-=")

        while True:
            opc = input("digite a operação(+, -, *, /): ")
          
            if opc in opc_list:
                if opc == opc_list[0]:
                    calc = f"{num1} + {num2} = {num1 + num2}"
                elif opc == opc_list[1]:
                    calc = f"{num1} - {num2} = {num1 - num2}"
                elif opc == opc_list[2]:
                    calc = f"{num1} * {num2} = {num1 * num2}"
                elif opc == opc_list[3]:
                    calc = f"{num1} / {num2} = {num1 / num2}"

                break
            else:
                print("valor invalido!!!")

        print(30 * "=-=")
        print(calc)
        print(30 * "=-=")

print("finalizando... ")
print(30 * "=-=")