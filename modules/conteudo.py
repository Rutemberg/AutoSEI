# importando a classe Inserir_Conteudo
from classes.Conteudo import Inserir_Conteudo
from util.funcoes import menu, criar_pasta  # funcao de criacao de menu e pasta
from util.log import log  # funcao de criacao de logs
from locale import LC_ALL, setlocale
import os

# funcao de insercao dos conteudos das disciplinas


def iniciar_insercao(disciplinas, configuracoes):
    setlocale(LC_ALL, 'pt_BR.utf-8')

    # criacao do menu
    menu("Inserir/Verificar todas as disciplinas",
         "Inserir disciplina especifica", "Verificar disciplinas que faltam")
    opcao = int(input("Digite a opção: "))

    # Se a opcao do menu for == 2 aramazenara o codigo em uma variavel
    os.system("cls")
    if opcao == 2:
        key = None
        while key == None:
            disciplina_codigo = int(input("Digite o código do conteúdo: "))
            # Pega a chave de um elemento da lista se o codigo digitado for encontrado
            key = next((index for (index, d) in enumerate(disciplinas)
                        if d["codigo_conteudo"] == disciplina_codigo), None)
            # Substitui a lista de disciplinas pela disciplina encontrada com a chave
            if key != None:
                log("app",
                    f"Disciplina {disciplinas[key]['nome_disciplina']} encontrada", "info")
                disciplinas = [disciplinas[key]]
            else:
                log("app",
                    f"Código de conteudo {disciplina_codigo} não encontrado", "warn")

    iniciar = input("Iniciar (Sim/Nao): ")
    iniciar = iniciar.upper()

    titulo_semana = configuracoes["semana"]
    pasta_atual = os.getcwd()  # Pega a localizacao da pasta atual

    if iniciar == "SIM":
    # Funcao criar_pasta(nome, path) para criar pasta com o nome e a localizacao atual
        pasta_log = criar_pasta("logs", pasta_atual)
        pasta_semanas = criar_pasta(titulo_semana, pasta_log)

        arquivo = f"{pasta_semanas}\{titulo_semana}"
        arquivo_obs = f"{pasta_semanas}\Disciplinas_que_faltam"
        arquivo_videos_sem_titulos = f"{pasta_semanas}\Videos_sem_temas"

    Processar = Inserir_Conteudo(iniciar)  # Iniciar caso a resposta seja sim
    Processar.abrir(configuracoes["site"])  # Abre o site
    # Loga com usuario e senha
    Processar.logar(configuracoes["usuario"], configuracoes["senha"])
    os.system("cls")

    for disciplina in disciplinas:  # For para percorrer as disciplinas

        # Se nao houver videos e a opcao for 3 fara um log com as disciplinas que faltam
        if [x for x in disciplina["videos"] if x['frame'] == ''] and opcao == 3:
            log(arquivo_obs,
                f"*{disciplina['professor']}* - {disciplina['nome_disciplina']}", "warn", True)
            # log(arquivo, f"{disciplina['professor']} - {disciplina['nome_disciplina']}", "", "info", True)
            # log(arquivo, "", "Videos indisponiveis !", "warn")

         # Se opcao for 1 ou 2 fara o processo de insercao
        elif opcao == 1 or opcao == 2:

            # Abre um arquivo de log e insere o titulo da disciplina
            log(arquivo,
                f"\n\n{disciplina['professor']} - {disciplina['nome_disciplina']}", "info", True)

            # Se existir videos para serem lançados prossiga com a inserção
            if [x for x in disciplina["videos"] if x['frame'] != '']:

                # Pesquisa a disciplina pela url e codigo
                Processar.pesquisar_conteudo(
                    configuracoes["url_conteudo"], disciplina["codigo_conteudo"])
                # Aguarda o carregamento do sistema
                Processar.aguardar_processo()
                # Seleciona a disciplina listada
                Processar.selecionar_disciplina()
                # Verifica se a semana em questão existe
                semana_existe = Processar.verificar_conteudo(
                    configuracoes["semana"])

                # Se a semana nao existir prossiga com a inserção
                if semana_existe == 0:

                    cont_titulo_video = 0
                    # Insere a semana
                    Processar.inserir_semana(configuracoes["semana"])
                    Processar.aguardar_processo()

                    for video in disciplina["videos"]:

                        cont_titulo_video += 1

                        if video["titulo"] != '':
                            titulo = video["titulo"]
                        else:
                            titulo = f'VIDEO {cont_titulo_video}'
                            log(arquivo_videos_sem_titulos,
                                f"*{disciplina['professor']}* - {disciplina['nome_disciplina']} - {titulo} sem tema", "warn", True, False)
                            log(arquivo,
                                f"{disciplina['professor']} - {disciplina['nome_disciplina']} - {titulo} sem tema", "warn")

                        # Adiciona o video
                        Processar.adicionar_video()
                        Processar.aguardar_processo()
                        # insere o video com titulo e frame
                        Processar.inserir_video(titulo, video["frame"])
                        Processar.aguardar_processo()

                        # Cria ou abre o log informando
                        log(arquivo, f"Video: {titulo} inserido", "info")
                        # Se a semana já existir
                else:
                    log(arquivo, f"{titulo_semana} já inserida !", "info")

            # Se não existir videos para serem lançados
            else:
                # Cria ou abre o log informando em dois arquivos
                log(arquivo_obs,
                    f"*{disciplina['professor']}* - {disciplina['nome_disciplina']}", "warn", True, False)
                log(arquivo, "Videos indisponiveis !", "warn")
