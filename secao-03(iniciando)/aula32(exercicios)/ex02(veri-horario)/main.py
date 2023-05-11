print("=-=" * 20)
hora = int(input("digite a hora em numero inteiro: "))
print("=-=" * 20)

if hora >= 0 and hora <= 11:
    print(f"são {hora} horas, Bom dia!")
elif hora >= 12 and hora <= 17:
    print(f"são {hora} horas, Boa Tarde!")
elif hora >= 18 and hora <= 23:
    print(f"são {hora} horas, Boa noite!") 
else:
    print("HORARIO INVALIDO!!!")

print("=-=" * 20)
