from os import system
from modulo_tarefas import showlist, showmenu, addlast

tarefas = []
desfeito = []

while True:
    opt = showmenu()
    system("cls")

    if opt == "1":
        showlist(tarefas)
    elif opt == "2":
        addlast(tarefas, desfeito)
        showlist(tarefas)
    elif opt == "3":
        addlast(desfeito, tarefas)
        showlist(tarefas)
    elif opt == "0":
        break
    else:
        tarefas.append(opt)
        
print("saindo...")