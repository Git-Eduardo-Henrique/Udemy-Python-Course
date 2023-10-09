def fatorial(num = 0):
    if num <= 1:
        return 1
    
    return num * fatorial(num - 1)

print("\033[31m", 30 * "=-=", "\033[m")
print(f"fatorial de 5: \033[31m{fatorial(5)}\033[m")
print(f"fatorial de 10: \033[31m{fatorial(10)}\033[m")
print("\033[31m", 30 * "=-=", "\033[m")