from modules.conteudo import iniciar_insercao
from modules.prova import iniciar_insercao_prova
from config.semana import disciplinas, configuracoes #Arquivo de configuraçao e lista de disciplinas
from config.prova import configuracao_prova


print(f"\nAUTOSEI\n\n")
print("1 - Videos")
print("2 - Provas (Ainda em construção)")
opcao = int(input("\n\nSelecione uma opção: "))

if opcao == 1:
    iniciar_insercao(disciplinas, configuracoes)
else:
    # iniciar_insercao_prova(disciplinas, configuracoes, configuracao_prova)
    pass

# Chamando a funcao iniciar insercao para iniciar o app
# iniciar_insercao(disciplinas, configuracoes)
# iniciar_insercao_prova(disciplinas, configuracoes, configuracao_prova)

