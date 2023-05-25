print(30 * "=-=")
print("calculadora com while")
print(30 * "=-=")

while True:
        opt = input("você deseja continuar? (n = não): ")
        print(30 * "=-=")

        if opt.upper() == "N":
            break

        try:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero: "))
        except:
            print(30 * "=-=")
            print("valor invalido!!!")
            print(30 * "=-=")

        opc_list = ("+", "-", "*", "/")
        while True:
            opc = input("digite a operação(+, -, *, /): ")

            if opc in opc_list:
                if opc == opc_list[0]:
                    calc = num1 + num2
                elif opc == opc_list[1]:
                    calc = num1 - num2
                elif opc == opc_list[2]:
                    calc = num1 * num2
                elif opc == opc_list[3]:
                    calc = num1 / num2

                print(30 * "=-=")
                print(f"sua conta deu o valor: {calc}")
                print(30 * "=-=")
                break
            else:
                print("valor invalido!!!")

print("finalizando... ")
print(30 * "=-=")