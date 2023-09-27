mega_lista = [
    1, 2, 3, True, (1, 0), {0, 2}, False, "Valor top", 1.54, {"nome": "Eduardo"}
]

print(30 * "\033[33m=-=", "\033[m")

for item in mega_lista:
    if isinstance(item, str):
        print(f"{item} = é uma \033[33mSTRING\033[m")

    elif isinstance(item, bool):
        print(f"{item} = é um \033[33mBOOLEAN\033[m")

    elif isinstance(item, (int, float)):
        print(f"{item} = é um \033[33mNUMERO\033[m")

    elif isinstance(item, tuple):
        print(f"{item} = é uma \033[33mTUPLA\033[m")

    elif isinstance(item, set):
        print(f"{item} = é um \033[33mSET\033[m")

    elif isinstance(item, dict):
        print(f"{item} = é um \033[33mDICIONARIO\033[m")

print(30 * "\033[33m=-=", "\033[m")