import logging
from datetime import datetime
from locale import LC_ALL, setlocale
setlocale(LC_ALL, 'pt_BR.utf-8')

def log(nome_do_arquivo, nome_evento, mensagem, modo, titulo=False):
    logger = logging.getLogger(f"{nome_evento}")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fl = logging.FileHandler(filename=f"{nome_do_arquivo}.log",encoding='utf-8')
    fl.setLevel(logging.DEBUG)

    if titulo == True:
        formatter = logging.Formatter(fmt='\n\n%(name)s\n')
    else:
        data = datetime.now()
        hora = data.strftime('%H')
        minuto = data.strftime('%M')
        segundo = data.strftime('%S')
        formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s',datefmt=f'%d/%m/%Y {hora}:{minuto}:{segundo}')

    ch.setFormatter(formatter)
    fl.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fl)

    if modo == "info":
        logger.info(f"{mensagem}")
    elif modo == "warn":
        logger.warning(f"{mensagem}")
    
    logger.removeHandler(ch)
    logger.removeHandler(fl)
