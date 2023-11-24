class Inutil():

    # permite utilizar o metodo sem self ou cls
    # sim é inutil
    @staticmethod
    def metodo_inutil():
        print("Oi")

print("\033[35m", 30 * "=-=", "\033[m")
Inutil.metodo_inutil()
print("\033[35m", 30 * "=-=", "\033[m")