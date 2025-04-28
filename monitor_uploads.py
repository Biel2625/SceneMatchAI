import time
import os
import subprocess

def monitorar_uploads():
    caminho_uploads = 'uploads'
    print(f"Monitorando uploads na pasta '{caminho_uploads}'...")

    arquivos_anteriores = set(os.listdir(caminho_uploads))

    while True:
        time.sleep(3)  # Verifica a cada 3 segundos
        arquivos_atuais = set(os.listdir(caminho_uploads))
        novos_arquivos = arquivos_atuais - arquivos_anteriores

        for novo_arquivo in novos_arquivos:
            if novo_arquivo.endswith('.txt'):
                print(f"Novo roteiro detectado: {novo_arquivo}")
                subprocess.run(["python", "processar_roteiro.py"])

        arquivos_anteriores = arquivos_atuais

if __name__ == "__main__":
    monitorar_uploads()
