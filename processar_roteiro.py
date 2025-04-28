import os
import time
import shutil

def processar_roteiro(nome_arquivo):
    """
    Simula o processamento de um roteiro.
    """
    caminho_uploads = os.path.join('uploads', nome_arquivo)
    caminho_resultado = os.path.join('processados', f"resultado_{nome_arquivo}")

    print(f"Processando o roteiro '{caminho_uploads}'...")
    time.sleep(2)  # Simula o tempo de processamento

    with open(caminho_resultado, 'w', encoding='utf-8') as f:
        f.write(f"Cena encontrada: {nome_arquivo.replace('.txt', '')} (duração: 5 segundos)\n")

    print(f"Resultado salvo em: {caminho_resultado}")
    print("Processamento concluído com sucesso!")

def verificar_uploads():
    """
    Verifica se há arquivos de roteiro enviados.
    """
    caminho_uploads = 'uploads'
    arquivos = os.listdir(caminho_uploads)
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith('.txt')]

    if not arquivos_txt:
        print("Nenhum roteiro encontrado.")
        return

    for roteiro in arquivos_txt:
        processar_roteiro(roteiro)
        # Move o roteiro original para a pasta 'processados'
        origem = os.path.join(caminho_uploads, roteiro)
        destino = os.path.join('processados', roteiro)
        shutil.move(origem, destino)
        print(f"Roteiro '{roteiro}' processado e movido para a pasta 'processados'.")

if __name__ == "__main__":
    print("Iniciando verificação de uploads...")
    verificar_uploads()
