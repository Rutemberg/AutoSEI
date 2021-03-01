from classes.Conteudo import Inserir_Conteudo

from SEMANAS.SEMANA import disciplinas, configuracoes
from datetime import datetime
from locale import LC_ALL, setlocale
import os
import pathlib

setlocale(LC_ALL, 'pt_BR.utf-8')

titulo_semana = configuracoes["semana"]
caminho_pasta = os.getcwd() + f"\SEMANAS\{titulo_semana}"
arquivo = f"{caminho_pasta}\{titulo_semana}.txt"
arquivo_obs = f"{caminho_pasta}\Disciplinas_que_faltam.txt"

if pathlib.Path(caminho_pasta).is_dir():
    print("Pasta já criada")
else:
    os.mkdir(caminho_pasta)

Processar = Inserir_Conteudo()
Processar.abrir(configuracoes["site"])
Processar.logar(configuracoes["usuario"], configuracoes["senha"])

with open(arquivo, "a", encoding="utf-8") as f:

    with open(arquivo_obs, "w", encoding="utf-8") as e:

        data = datetime.now()
        f.write(f"{data.strftime('%d de %B de %Y')}\n")
        e.write(
            f"{data.strftime('%d de %B de %Y')}\n\n*Professores que ainda faltam postar*\n\n")

        for disciplina in disciplinas:

            Processar.pesquisar_conteudo(
                configuracoes["url_conteudo"], disciplina["codigo_conteudo"])
            Processar.aguardar_processo()
            Processar.selecionar_disciplina()
            semana_existe = Processar.verificar_conteudo(
                configuracoes["semana"])

            f.write(
                f"\n\n{disciplina['professor']} - {disciplina['nome_disciplina']}\n\n")

            if semana_existe == 0:
                if len(disciplina["videos"]) > 0:
                    cont_titulo_video = 0
                    Processar.inserir_semana(configuracoes["semana"])
                    Processar.aguardar_processo()

                    for video in disciplina["videos"]:

                        cont_titulo_video += 1
                        titulo = video["titulo"] if video[
                            "titulo"] != '' else f'VIDEO {cont_titulo_video}'

                        Processar.adicionar_video()
                        Processar.aguardar_processo()
                        Processar.inserir_video(titulo, video["frame"])
                        Processar.aguardar_processo()

                        horas = datetime.now()
                        f.write(
                            f"{horas.strftime('%H:%M:%S')}   Video: {titulo} inserido \n")
                    f.write(f"{50*'_'}\n")
                else:
                    mensagem = f"*{disciplina['professor']}* - {disciplina['nome_disciplina']}\n"
                    e.write(mensagem)
                    f.write(f"{horas.strftime('%H:%M:%S')}   Videos indisponiveis !\n{50*'_'}\n")
            else:
                horas = datetime.now()
                f.write(
                    f"{horas.strftime('%H:%M:%S')}   {titulo_semana} já inserida !\n{50*'_'}\n")

    f.write("\n\n\n\n")

# driver.quit()
