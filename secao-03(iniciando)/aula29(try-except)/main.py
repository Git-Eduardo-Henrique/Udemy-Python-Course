print("=-=" * 30)
valor = input("Digite um valor para ver seu dobro: ")
print("=-=" * 30)

try:
    num = float(valor)
    print(f"o dobro de {num} é {num * 2}")
except:
    print("digite apenas numeros!")

print("=-=" * 30)
