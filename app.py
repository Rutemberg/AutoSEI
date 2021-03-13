from modules.conteudo import iniciar_insercao
from modules.prova import iniciar_insercao_prova
import json
import os

path = os.getcwd()

with open(f"{path}/config/config.json", encoding="utf8") as file:
    configuracoes = file.read()
    configuracoes = json.loads(configuracoes)

with open(f"{path}/config/semana.json", encoding="utf8") as file:
    disciplinas = file.read()
    disciplinas = json.loads(disciplinas)


print(f"\nAUTOSEI\n\n")
print("| 1 - Videos")
print("| 2 - Provas (Ainda em construção)")
opcao = int(input("\n\nSelecione uma opção: "))

if opcao == 1:
    iniciar_insercao(disciplinas, configuracoes)
else:
    # iniciar_insercao_prova(disciplinas, configuracoes, configuracao_prova)
    pass



