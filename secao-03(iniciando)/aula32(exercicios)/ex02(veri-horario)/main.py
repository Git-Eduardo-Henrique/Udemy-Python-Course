print("=-=" * 20)
hora = input("digite a hora em numero inteiro: ")
print("=-=" * 20)
try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print(f"são {hora_int} horas, Bom dia!")
    elif hora_int >= 12 and hora_int <= 17:
        print(f"são {hora_int} horas, Boa Tarde!")
    elif hora_int >= 18 and hora_int <= 23:
        print(f"são {hora_int} horas, Boa noite!") 
    else:
        print("HORARIO INVALIDO!!!")

except:
    print("HORARIO INVALIDO!!!!")

print("=-=" * 20)