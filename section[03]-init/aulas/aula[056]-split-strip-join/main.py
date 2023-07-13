frase = "  Frase muito top, Among Us   "
frase_split = frase.split(",") # divide a frase pela virgula
frase_strip = []

for index, item in enumerate(frase_split):
    # remove os espaços da esquerda e direita
    frase_strip.append(item.strip())

frase_join = " | ".join(frase_strip) # junta a frase e divide por |

print(30 * "\033[35m=-=\033[m", "\033[m")

print(f"frase original: {frase}\nfrase com split: {frase_split}\nfrase split com strip: {frase_strip}\n"
      f"frase strip com join: {frase_join}")

print(30 * "\033[35m=-=\033[m", "\033[m")