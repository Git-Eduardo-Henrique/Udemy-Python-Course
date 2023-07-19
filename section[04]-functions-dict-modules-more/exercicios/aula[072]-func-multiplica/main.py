def multiplica(*args):
    total = 1
    for num in args:
        total *= num

    return total

def parimpar(num):
    return num % 2 == 0


mult = multiplica(9, 2, 3, 21, 22, 2, 5)
veri_mult = parimpar(mult)

print(30 * "\033[31m=-=", "\033[m")
print(f"o resultado da multiplicação é: {mult}\neste numero é par?: {veri_mult}")
print(30 * "\033[31m=-=", "\033[m")