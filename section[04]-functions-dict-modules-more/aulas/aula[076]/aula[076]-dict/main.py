pessoa = {
    "nome": "Eduardo",
    "sobrenome": "Henrique",
    "idade" : 18,
    "sexo" : "masculino",
    "enderecos" : [
        {
            "rua" : "Rua falano da Silva",
            "num" : 921
        },
        {
           "rua" : "Rua falano da Silva 2",
            "num" : 921 
        }
    ]
}


print(30 * "\033[34m=-=", "\033[m")

for key in pessoa:
    print(f"{key} = {pessoa[key]}")

print(30 * "\033[34m=-=", "\033[m")