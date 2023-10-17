class Camera:
    def __init__(self, nome="", filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"\033[31m{self.nome}\033[m já está filmando | \033[31m{self.filmando}\033[m")
            return
        
        self.filmando = True
        print(f"\033[31m{self.nome}\033[m começou a filmar | \033[31m{self.filmando}\033[m")

    def parar_filmar(self):
        if not self.filmando:
            print(f"\033[31m{self.nome}\033[m não está filmando | \033[31m{self.filmando}\033[m")
            return
        
        self.filmando = False
        print(f"\033[31m{self.nome}\033[m parou de filmar | \033[31m{self.filmando}\033[m")

tekpix = Camera(nome="tekpix")

print("\033[31m", 30 * "=-=", "\033[m")
tekpix.parar_filmar()
tekpix.filmar()
tekpix.filmar()
tekpix.parar_filmar()
print("\033[31m", 30 * "=-=", "\033[m")