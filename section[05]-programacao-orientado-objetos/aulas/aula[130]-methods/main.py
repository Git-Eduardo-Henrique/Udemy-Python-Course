class Connect():
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_user(cls, user, password):
        connect = cls()
        connect.user = user
        connect.password = password
        return connect

    @staticmethod
    def log(msg):
        print("log: ", msg)

conexao1 = Connect()
conexao1.set_user("Eduardo")
conexao1.set_password("senhatop123")

conexao2 = Connect.create_user("Fulano", "FX039-23  ")

print("\033[36m", 30 * "=-=", "\033[m")

print(f"Conexão 1 | local: {conexao1.host} | user: {conexao1.user} | password: {conexao1.password}")
print(f"Conexão 2 | local: {conexao2.host} | user: {conexao2.user} | password: {conexao2.password}")
Connect.log("esta é a mensagem de log")

print("\033[36m", 30 * "=-=", "\033[m")