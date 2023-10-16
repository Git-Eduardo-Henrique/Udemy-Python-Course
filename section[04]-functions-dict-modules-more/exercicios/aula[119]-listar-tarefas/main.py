from os import system
from modulo_tarefas import showlist, showmenu, addlast, jsonsave, jsonload

tarefas = jsonload()
desfeito = []

running = True
while running:
    opt = showmenu()
    system("cls")

    comandos = {
        "1": lambda: showlist(tarefas),
        "2": lambda: addlast(tarefas, desfeito),
        "3": lambda: addlast(desfeito, tarefas),
        "adicionar": lambda: tarefas.append(opt)
    }

    if opt == "0":
            break

    if comandos.get(opt) is not None:
        comando = comandos.get(opt)
    else:
        comando = comandos["adicionar"]

    comando()
    jsonsave(tarefas=tarefas)

    # if opt == "1":
    #     showlist(tarefas)
    # elif opt == "2":
    #     addlast(tarefas, desfeito)
    #     showlist(tarefas)
    # elif opt == "3":
    #     addlast(desfeito, tarefas)
    #     showlist(tarefas)
    # elif opt == "0":
    #     break
    # else:
    #     tarefas.append(opt)
                
print("saindo...")