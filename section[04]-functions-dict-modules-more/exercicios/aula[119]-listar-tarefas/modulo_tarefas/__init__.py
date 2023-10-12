def linha():
    print(30 * "\033[33m=-=", "\033[m")

def showmenu():
    linha()
    print(f"{'Comandos:':^90}")
    print("\033[33m[ 0 ] - Sair \n[ 1 ] - Listar \n[ 2 ] - Desfazer \n[ 3 ] - Refazer\033[m")
    linha()

    return input("Adicione uma \033[33mtarefa ou comando\033[m: ")

def showlist(lista):
    linha()
    print(f"{'Tarefas:':^90}")
    print("\033[33m")

    if len(lista) > 0:
        for index, item in enumerate(lista):
            print(f"[ {index + 1} ] - {item}")
    else:
        print("SEM ITEMS PARA LISTAR")

    print("\033[m")

def addlast(lista_retirar, lista_adicionar):
    if len(lista_retirar) > 0:
        removida = lista_retirar.pop()

        lista_adicionar.append(removida)
    else:
        print("SEM ITEMS PARA ESTA AÇÃO")