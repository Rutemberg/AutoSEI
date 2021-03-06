from modules.conteudo import iniciar_insercao
from modules.prova import iniciar_insercao_prova
from config.SEMANA import disciplinas, configuracoes #Arquivo de configuraçao e lista de disciplinas
from config.prova import configuracao_prova

# Chamando a funcao iniciar insercao para iniciar o app
# iniciar_insercao(disciplinas, configuracoes)
iniciar_insercao_prova(disciplinas, configuracoes, configuracao_prova)