from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys


class Inserir_Conteudo:

    # Inicia o driver caso a resposta seja sim ou s
    def __init__(self, iniciar):
        if (iniciar == "SIM" or iniciar == "S"):
            self.driver = Chrome()
        else:
            sys.exit()

    # abre o site pela url
    def abrir(self, url):
        self.driver.get(url)
    
    # Aguardar ate que a mensagem de loading suma
    def aguardar_processo(self):
        wait = WebDriverWait(self.driver, 10)
        # Aguarda até que o elemento(loading do sistema) suma da tela
        wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'rf-st-start')))
        
    # Loga no site usando o usuario e senha
    def logar(self, usuario, senha):
        # procura os elementos
        usuario_campo = self.driver.find_element_by_id("formLogin:username")
        senha_campo = self.driver.find_element_by_id("formLogin:senha")
        # Insere os valores nos campos
        usuario_campo.send_keys(usuario)
        senha_campo.send_keys(senha)
        # Procura o botao e clica
        logar = self.driver.find_element_by_id("formLogin:btLogin")
        logar.click()

    # Pesquisa o conteudo
    def pesquisar_conteudo(self, url_conteudo, codigo_conteudo):
        self.driver.get(url_conteudo) # navegue ate a url
        # Usando o select encontra o elemento select do html
        consultar_por = Select(self.driver.find_element_by_id("form:consulta"))
        # Seleciona o valor
        consultar_por.select_by_value("codigoConteudo")

        self.aguardar_processo()

        # Consulta pelo codigo do conteudo 
        valor_consulta = self.driver.find_element_by_id("form:valorConsulta")
        valor_consulta.clear() # limpa o campo
        valor_consulta.send_keys(codigo_conteudo) # Escreve o codigo
        # Clica no botao consultar 
        consultar = self.driver.find_element_by_id("form:consultar")
        consultar.click()

    # Seleciona e clica na disciplina encontrada, somente a primeira e unica encontrada
    def selecionar_disciplina(self):
        click_disciplina = self.driver.find_element_by_id(
            "form:items:0:descricao")
        click_disciplina.click()

    # Verifica pelo texto se o conteudo existe
    def verificar_conteudo(self, elem):
        conteudo_existe = self.driver.find_elements_by_link_text(f"{elem}")
        return len(conteudo_existe)

    # Insere o titulo da semana
    def inserir_semana(self, semana):
        titulo_unidade = self.driver.find_element_by_id(
            "form:unidadeConteudoTitulo") # Pega o input pelo id
        titulo_unidade.send_keys(semana) # Digita o valor
        adicionar = self.driver.find_element_by_xpath(
            "//*[@id='form:j_idt595']") # pega o botao
        adicionar.click() # clica para salvar

    # Adiciona pegando a ultima semana inserida
    def adicionar_video(self):
        self.driver.find_elements_by_xpath(
            "//*[@title='Adicionar Página']")[-1].click()

    # Insere os videos por titulo e frame
    def inserir_video(self, titulo, frame):

        # Script para inserir o valor em um documento por innerHTML
        self.driver.execute_script(
            'document.getElementsByClassName("cke_wysiwyg_frame cke_reset")[0].contentDocument.body.innerHTML = ' + f"`{frame}`")

        # Escreve o titulo no input encontrado
        titulo_video = self.driver.find_element_by_id("formNovaPagina:titulo")
        titulo_video.send_keys(titulo)

        self.driver.execute_script(
            'document.getElementById("formNovaPagina:salvar").click()')

