print("=-=" * 20)
num = input("digite um numero inteiro!: ")

try:
    int_num = int(num)

    if int_num % 2 == 0:
        print("=-=" * 20)
        print("Seu numero é Par")
    else:
        print("=-=" * 20)
        print("Seu numero é Impar")


except:
    print("=-=" * 20)
    print("VOCÊ NÃO DIGITOU UM NUMERO INTEIRO!!!!")
 
print("=-=" * 20)
