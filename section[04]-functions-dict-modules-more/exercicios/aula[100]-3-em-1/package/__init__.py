def show_list_items(your_dict = {}, title = ""):
    print()
    print(30 * "\033[31m=-=", "\033[m")
    print(f"{title:^90}")
    print(30 * "\033[31m=-=", "\033[m")

    for item in your_dict:
        print(f"{item['nome']} = \033[31mR${item['preco']}\033[m")

    print(30 * "\033[31m=-=", "\033[m")

def increase_prices(your_dict = {}, increase = 0):
    for item in your_dict:
        item["preco"] += item["preco"] * increase

def increasing_decreasing(your_dict = {}, key = "", decre=False):
    # orderna em order decrescente ou crescente
    # key = qual a chave do dict 
    # decre = True : decrescente
    return sorted(your_dict, key=lambda item: item[key], reverse=decre)