frase = "frase muito boa"
nova_frase = ""

for letra in frase:
    print(f"letra atual: {letra}")
    nova_frase += f"*{letra}"

print(f"{nova_frase}*")