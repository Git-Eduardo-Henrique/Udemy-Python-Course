from decimal import Decimal

num1 = 0.1
num2 = 0.7
num3 = num1 + num2

print(30 * "\033[34m=-=\033[m", "\033[m")
print(f"{num1} + {num2}")
# round formata o float sem adicionar casas 
print(f"sem formatação: {num3}\nformatação de f-string: {num3:.2f}\nformatação com round: {round(num3, 2)}")

num1d = Decimal("0.1")
num2d = Decimal("0.7")
num3d = num1d + num2d
print(f"formatação com Decimal: {num3d}")

print(30 * "\033[34m=-=\033[m", "\033[m")