frase = "  Frase muito top, Among Us   "
frase_split = frase.split(",")
frase_strip = []

for index, item in enumerate(frase_split):
    frase_strip.append(item.strip())

frase_join = " | ".join(frase_strip)

print(30 * "\033[35m=-=\033[m", "\033[m")

print(f"frase original: {frase}\nfrase com split: {frase_split}\nfrase split com strip: {frase_strip}\n"
      f"frase strip com join: {frase_join}")

print(30 * "\033[35m=-=\033[m", "\033[m")