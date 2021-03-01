from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys


class Inserir_Conteudo:

    def __init__(self, iniciar):
        if (iniciar == "SIM" or iniciar == "S"):
            self.driver = Chrome()
        else:
            sys.exit()

    def abrir(self, site):
        self.driver.get(site)

    def aguardar_processo(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.invisibility_of_element((By.CLASS_NAME, 'rf-st-start')))

    def logar(self, usuario, senha):
        usuario_campo = self.driver.find_element_by_id("formLogin:username")
        senha_campo = self.driver.find_element_by_id("formLogin:senha")

        usuario_campo.send_keys(usuario)
        senha_campo.send_keys(senha)

        logar = self.driver.find_element_by_id("formLogin:btLogin")
        logar.click()

    def pesquisar_conteudo(self, url_conteudo, codigo_conteudo):
        self.driver.get(url_conteudo)
        consultar_por = Select(self.driver.find_element_by_id("form:consulta"))
        consultar_por.select_by_value("codigoConteudo")

        self.aguardar_processo()

        valor_consulta = self.driver.find_element_by_id("form:valorConsulta")
        valor_consulta.clear()
        valor_consulta.send_keys(codigo_conteudo)

        consultar = self.driver.find_element_by_id("form:consultar")
        consultar.click()

    def selecionar_disciplina(self):
        click_disciplina = self.driver.find_element_by_id(
            "form:items:0:descricao")
        click_disciplina.click()

    def verificar_conteudo(self, elem):
        conteudo_existe = self.driver.find_elements_by_link_text(f"{elem}")
        return len(conteudo_existe)

    def inserir_semana(self, semana):
        titulo_unidade = self.driver.find_element_by_id(
            "form:unidadeConteudoTitulo")
        titulo_unidade.send_keys(semana)
        adicionar = self.driver.find_element_by_xpath(
            "//*[@id='form:j_idt595']")
        adicionar.click()

    def adicionar_video(self):
        self.driver.find_elements_by_xpath(
            "//*[@title='Adicionar Página']")[-1].click()

    def inserir_video(self, titulo, frame):

        self.driver.execute_script(
            'document.getElementsByClassName("cke_wysiwyg_frame cke_reset")[0].contentDocument.body.innerHTML = ' + f"`{frame}`")

        titulo_video = self.driver.find_element_by_id("formNovaPagina:titulo")
        titulo_video.send_keys(titulo)

        self.driver.execute_script(
            'document.getElementById("formNovaPagina:salvar").click()')

