for cont in range(10):
    if cont == 2:
        print("2 não sera mostrado")
        continue

    if cont == 8:
        print("não foi para o else")
        break
       

    for column in range(5):
        print(cont, column)

else:
    print("terminado")