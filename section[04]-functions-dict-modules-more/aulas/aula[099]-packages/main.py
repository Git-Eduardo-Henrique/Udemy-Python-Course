from modulo_package.modulo import soma

num1 = num2 = 0

print(30 * "\033[34m=-=", "\033[m")

num1 = int(input("digite o \033[34mprimeiro numero\033[m: "))
num2 = int(input("digite o \033[34msegundo numero\033[m: "))

print(30 * "\033[34m=-=", "\033[m")
print(f"{num1} + {num2} = \033[34m{soma(num1, num2)}\033[m")
print(30 * "\033[34m=-=", "\033[m")