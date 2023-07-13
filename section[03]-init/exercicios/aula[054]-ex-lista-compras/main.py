from time import sleep

lista = list() # lista de produtos

while True: 
    opt = 0
    print(30 * "\033[31m=-=\033[m", "\033[m")
    print("1 - listar\n2 - adicionar\n3 - apagar\n4 - sair")
    print(30 * "\033[31m=-=\033[m", "\033[m")

    while opt > 4 or opt <= 0:  # se a opção não existir
        opt = int(input("sua opção: "))

    if opt == 1: # listagem de produtos
        print(30 * "\n")
        print(30 * "\033[31m=-=\033[m", "\033[m")

        # criar uma tabela de produtos caso a lista não estiver vazia
        if len(lista) == 0:
            print("sem valores para mostrar!")
        else:
            for index, item in enumerate(lista):
                print(f"\033[31m{index+1}\033[m | nome: \033[31m{item[0]}\033[m | valor: "
                    f"\033[31mR${item[1]}\033[m")
                sleep(0.5)

        sleep(0.5)

    elif opt == 2: # adicionar produtos
        print(30 * "\n")
        print(30 * "\033[31m=-=\033[m", "\033[m")

        nome = str(input("digite o nome: "))
        valor = float(input("digite o valor: R$"))

        sleep(0.5)
        
        # formata o valor para o real | ex: 20,23
        valor = f"{valor:.2f}".replace(".", ",")
        lista.append((nome, valor))

        print(f"\033[31m{nome}\033[m foi adicionado com sucesso!!!")

    elif opt == 3: # deletar produtos
        print(30 * "\n")
        print(30 * "\033[31m=-=\033[m", "\033[m")

        # caso a lista não estiver vazia
        if len(lista) == 0:
            print("sem valores para deletar!")

        else:
            ind = int(input(f"index para deletar: "))           
            sleep(0.5)

            # tenta deletar o valor caso ele exista
            try:
                lista[ind]          
            except IndexError:
                print(f"\033[31mErro! Index não encontrado - digite um index de ({0} a {len(lista) - 1})\033[m")            
            else:
                print(f"item \033[31m{lista[ind][0]}\033[m deletado com sucesso!")
                del lista[ind]

    elif opt == 4: # fechar
        print(30 * "\033[31m=-=\033[m", "\033[m")
        break