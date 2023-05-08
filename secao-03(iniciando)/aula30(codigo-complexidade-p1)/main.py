print("=-=" * 30)

# minusculo para variaveis que vão mudar
velocidade_carro = 61
km_estrada = 90

# maiusculo para variaveis que não vão mudar
RADAR_1 = 60
LOCAL_1 = 100

print(f"voce esta a {velocidade_carro}km/h e ja andou {km_estrada}km, faltam {LOCAL_1 - km_estrada}km para chegar")
if velocidade_carro > RADAR_1:
    print("voce ultrapassou a velocidade permitida! multado")
else:
    print("Velocidade ok pode continuar")

print("=-=" * 30)