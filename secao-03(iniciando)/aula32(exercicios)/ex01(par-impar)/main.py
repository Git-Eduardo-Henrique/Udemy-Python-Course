print("=-=" * 20)
num = input("digite um numero inteiro!: ")
print("=-=" * 20)

try:
    int_num = int(num)

    if int_num % 2 == 0:
        print("Seu numero é Par")
    else:
        print("Seu numero é Impar")


except:
    print("=-=" * 20)
    print("VOCÊ NÃO DIGITOU UM NUMERO INTEIRO!!!!")
 
print("=-=" * 20)
