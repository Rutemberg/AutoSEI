import os
import pathlib
from util.log import log
from datetime import datetime

def menu(*args):
    os.system("cls")
    print(f"\nAUTOSEI\n\n")
    for key, item in enumerate(args):
        print(f"{key+1}. {item}")
    print(f"\n{len(args)+1}. Sair\n\n\n")


def criar_pasta(nome_da_pasta, pasta_atual):
    caminho_pasta = os.path.join(pasta_atual, nome_da_pasta)
    if pathlib.Path(caminho_pasta).is_dir():
        log("app", f"A pasta {nome_da_pasta} já existe", "info")
        return caminho_pasta
    else:
        try:
            os.mkdir(caminho_pasta)
            log("app", f"Pasta {nome_da_pasta} criada", "info")
            return caminho_pasta
        except OSError as error:
            print(error)

def tempo(hora_inicial, hora_final):
    hora_inicial= datetime.strptime(hora_inicial, "%d/%m/%Y %H:%M:%S")
    hora_final = datetime.strptime(hora_final, "%d/%m/%Y %H:%M:%S")

    dif = hora_final - hora_inicial

    return dif