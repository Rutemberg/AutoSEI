from classes.Conteudo import Inserir_Conteudo
from config.SEMANA import disciplinas, configuracoes
from util.funcoes import menu,criar_pasta
from util.log import log
from locale import LC_ALL, setlocale
import os
import pathlib

setlocale(LC_ALL, 'pt_BR.utf-8')

menu("Inserir/Verificar todas as disciplinas", "Inserir disciplina especifica", "Verificar disciplinas que faltam")
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
pasta_atual = os.getcwd()
pasta_log = criar_pasta("logs", pasta_atual)
pasta_semanas = criar_pasta(titulo_semana, pasta_log)

arquivo = f"{pasta_semanas}\{titulo_semana}"
arquivo_obs = f"{pasta_semanas}\Disciplinas_que_faltam"


Processar = Inserir_Conteudo(iniciar)
Processar.abrir(configuracoes["site"])
Processar.logar(configuracoes["usuario"], configuracoes["senha"])
os.system("cls")

for disciplina in disciplinas:

    if len(disciplina["videos"]) == 0 and opcao == 3:
        log(arquivo_obs, "", f"{disciplina['professor']} - {disciplina['nome_disciplina']}", "warn", False)
        # log(arquivo, f"{disciplina['professor']} - {disciplina['nome_disciplina']}", "", "info", True)
        # log(arquivo, "", "Videos indisponiveis !", "warn")

    elif opcao == 1 or opcao == 2:
        Processar.pesquisar_conteudo(
            configuracoes["url_conteudo"], disciplina["codigo_conteudo"])
        Processar.aguardar_processo()
        Processar.selecionar_disciplina()
        semana_existe = Processar.verificar_conteudo(
            configuracoes["semana"])

        log(arquivo, f"{disciplina['professor']} - {disciplina['nome_disciplina']}", "", "info", True)

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

                    log(arquivo, "", f"Video: {titulo} inserido", "info")
            else:
                log(arquivo_obs, f"{disciplina['professor']} - {disciplina['nome_disciplina']}", "warn", "", True)
                log(arquivo, "", "Videos indisponiveis !", "warn")

        else:
            log(arquivo, "", f"{titulo_semana} já inserida !", "info")

