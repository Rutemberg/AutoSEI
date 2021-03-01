from classes.Conteudo import Inserir_Conteudo
from SEMANAS.SEMANA import disciplinas, configuracoes
from util.funcoes import menu
from datetime import datetime
from locale import LC_ALL, setlocale
import os
import pathlib

setlocale(LC_ALL, 'pt_BR.utf-8')

menu(os, "Inserir/Verificar tudo", "Inserir disciplina especifica", "Verificar disciplinas que faltam")
opcao = int(input("Digite a opção: "))

if opcao == 2:
    os.system("cls")
    disciplina_codigo = int(input("Digite o código do conteúdo: "))
    key = next((index for (index, d) in enumerate(disciplinas)
                  if d["codigo_conteudo"] == disciplina_codigo), None)
    disciplinas = [disciplinas[key]]

iniciar = input("Iniciar (Sim/Nao): ")
iniciar = iniciar.upper()


titulo_semana = configuracoes["semana"]
caminho_pasta = os.getcwd() + f"\SEMANAS\{titulo_semana}"
arquivo = f"{caminho_pasta}\{titulo_semana}.txt"
arquivo_obs = f"{caminho_pasta}\Disciplinas_que_faltam.txt"

if pathlib.Path(caminho_pasta).is_dir():
    print("Usando pasta já criada")
else:
    os.mkdir(caminho_pasta)

Processar = Inserir_Conteudo(iniciar)
Processar.abrir(configuracoes["site"])
Processar.logar(configuracoes["usuario"], configuracoes["senha"])

with open(arquivo, "a", encoding="utf-8") as f:

    with open(arquivo_obs, "w", encoding="utf-8") as e:

        data = datetime.now()
        f.write(f"{data.strftime('%d de %B de %Y')}\n")
        e.write(f"{data.strftime('%d de %B de %Y')}\n\n*Professores que ainda faltam postar*\n\n")

        for disciplina in disciplinas:

            if len(disciplina["videos"]) == 0 and opcao == 3:
                horas = datetime.now()
                e.write(f"*{disciplina['professor']}* - {disciplina['nome_disciplina']}\n")
                f.write(f"\n\n{disciplina['professor']} - {disciplina['nome_disciplina']}\n\n")
                f.write(f"{horas.strftime('%H:%M:%S')}   Videos indisponiveis !\n{50*'_'}\n")

            elif opcao == 1 or opcao == 2:
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
                        e.write(f"*{disciplina['professor']}* - {disciplina['nome_disciplina']}\n")
                        f.write(f"{horas.strftime('%H:%M:%S')}   Videos indisponiveis !\n{50*'_'}\n")
                else:
                    horas = datetime.now()
                    f.write(
                        f"{horas.strftime('%H:%M:%S')}   {titulo_semana} já inserida !\n{50*'_'}\n")

    f.write("\n\n\n\n")

# driver.quit()
