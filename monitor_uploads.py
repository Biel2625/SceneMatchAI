import os
import time

def monitorar_pasta(pasta):
    print("Monitorando:", pasta)
    arquivos_anteriores = set(os.listdir(pasta))

    while True:
        time.sleep(5)
        arquivos_atuais = set(os.listdir(pasta))
        novos = arquivos_atuais - arquivos_anteriores

  if novos:print("Novos arquivos encontrados:", novos)
            # Aqui você pode acionar o processamento ou envio

        arquivos_anteriores = arquivos_atuais