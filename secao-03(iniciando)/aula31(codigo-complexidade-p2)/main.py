print("=-=" * 30)

# minusculo para variaveis que vão mudar
velocidade_carro = 61
km_estrada = 100

# maiusculo para variaveis que não vão mudar
RADAR_1 = 60
LOCAL_1 = 100
RAIO_RADAR = 1

vel_passou_radar = velocidade_carro > RADAR_1
passou_radar = km_estrada >= (LOCAL_1 - RAIO_RADAR) and km_estrada <= (LOCAL_1 + RAIO_RADAR)
multado = vel_passou_radar and passou_radar

print(f"voce esta a {velocidade_carro}km/h e andou {km_estrada}km")

if vel_passou_radar:
    print("Voce passou da velocidade do radar")

if passou_radar:
    print("Voce possou pelo radar")

if multado:
    print("Voce foi multado! em 1.000.000 kwansas")

print("=-=" * 30)