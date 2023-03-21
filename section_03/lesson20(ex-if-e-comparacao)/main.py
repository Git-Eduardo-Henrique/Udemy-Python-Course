primeiro_valor = input("digite o primeiro valor: ")
segundo_valor = input("digite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"o primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor})")
elif segundo_valor > primeiro_valor:
    print(f"o segundo valor ({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})")
else:
    print(f"os valores são iguais")
