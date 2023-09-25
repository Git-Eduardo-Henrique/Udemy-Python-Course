# | = union (une os valores dos sets sem repetir )
# & = intersetion ( une apenas os itens repetidos dos sets )
# - = apenas itens que não repetem presentes no primeiro set 
# ^ = apenas itens que não repetem nos sets

set1 = {1, 2, 3}
set2 = {2, 3, 4}

setuni = set1 | set2
setinter = set1 & set2
set3 = set1 - set2
set4 = set1 ^ set2

print(30 * "\033[35m=-=", "\033[m")
print(f"primeiro set = {set1}\nsegundo set = {set2}")
print(30 * "\033[35m=-=", "\033[m")
print(f"set union = {setuni}\nset intersetion = {setinter}\nset - = {set3}\n"
      f"set ^ = {set4}")
print(30 * "\033[35m=-=", "\033[m")