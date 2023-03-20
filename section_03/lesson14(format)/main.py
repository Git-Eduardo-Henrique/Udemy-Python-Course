a = " letra 'A' "
b = " letra 'B' "
c = " letra 'C' "

frase = "a={letra1}, b={letra2}, c={letra3}"

# .format faz o mesmo que as f strings so que pior
print(frase.format(letra1=a, letra2=b, letra3=c))