from copy import deepcopy
import package

produtos = novos_precos = decre_order = cre_order = []

produtos =[
    {"nome": "Mi 8 lite", "preco": 900},
    {"nome": "Iphone 15", "preco": 14000},
    {"nome": "S23 ULTRA", "preco": 11000},
    {"nome": "Nokia", "preco": 150}
]

novos_precos = deepcopy(produtos)
package.increase_prices(novos_precos, 0.1)

decre_order = package.increasing_decreasing(deepcopy(produtos), key="nome", decre=True)
cre_order = package.increasing_decreasing(deepcopy(produtos), key="preco")

package.show_list_items(your_dict=produtos, title="LISTA ORIGINAL")
package.show_list_items(your_dict=novos_precos, title="10% DE AUMENTO")
package.show_list_items(your_dict=decre_order, title="NOMES DECRECENTE")
package.show_list_items(your_dict=cre_order, title="PRECO CRECENTE")