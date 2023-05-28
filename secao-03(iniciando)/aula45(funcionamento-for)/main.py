frase = 'frase util'
# puxa o valor na memoria
iterfrase = iter(frase)

# o for internamente funcionaria assim:
while True:
    try:
        # next = mostrar a proxima posição na memoria
        print(next(iterfrase))

    except StopIteration:  # erro que da apos não acabar a string
        break

print("\n")

# funciona igual este for:
for letra in frase:
    print(letra)