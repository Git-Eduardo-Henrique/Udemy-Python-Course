import importlib

print(30 * "\033[33m=-=", "\033[m")
import modulo

for num in range(1, 11):
    # recarrega o modulo
    print(num)
    importlib.reload(modulo)