from os import getcwd
from json import dump, load
from main import Pessoa

directory = f"{getcwd()}\\section[05]-programacao-orientado-objetos\\exercicios\\aula[127]-json-__dict__" \
            f"\\aula[127]_data.json"

def save_json(dados):
    with open(directory, "w+") as file:
        dump(dados, file, indent=2)

        for item in dados:
            print(item)

def load_json():
    try:
        with open(directory, "r") as file:
            carregado = load(file)
            return carregado
    except:
        return []