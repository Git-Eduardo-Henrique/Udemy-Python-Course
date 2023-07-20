def multilicador(valor = 0):

    def multiplica(numero = 0):
        return numero * valor
    
    return multiplica
    

print(30 * "\033[34m=-=", "\033[m")

num = int(input("Digite um numero inteiro: "))

duplicar = multilicador(2)
triplicar = multilicador(3)
quadruplicar = multilicador(4)

print(30 * "\033[34m=-=", "\033[m")
print(f"duplicado: {duplicar(num)}\ntriplicar: {triplicar(num)}\nquadruplicar: {quadruplicar(num)}")
print(30 * "\033[34m=-=", "\033[m")