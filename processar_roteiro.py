import os
import time
import random

def simular_busca_cena(descricao):
    """
    Simula encontrar uma cena baseada na descrição.
    """
    duracao = random.randint(3, 5)  # duração aleatória entre 3 e 5 segundos
    print(f"Encontrada cena para: '{descricao}' (duração: {duracao} segundos)")
    time.sleep(1)  # Simula o tempo de busca

def processar_roteiro(nome_arquivo):
    """
    Lê o roteiro e simula a busca de cenas para cada ação.
    """
    caminho_arquivo = os.path.join('uploads', nome_arquivo)

    print(f"Processando o roteiro '{caminho_arquivo}'...")
    
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("O roteiro está vazio.")
                return

            for linha in linhas:
                linha = linha.strip()
                if linha:
                    simular_busca_cena(linha)
        
        print("\nProcessamento do roteiro concluído com sucesso!")
    
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")

def verificar_uploads():
    """
    Verifica se há arquivos de roteiro enviados.
    """
    uploads_dir = 'uploads'
    if not os.path.exists(uploads_dir):
        print("Pasta 'uploads' não encontrada.")
        return

    arquivos = os.listdir(uploads_dir)
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith(".txt")]

    if not arquivos_txt:
        print("Nenhum roteiro encontrado.")
        return

    for roteiro in arquivos_txt:
        processar_roteiro(roteiro)

if __name__ == "__main__":
    print("Iniciando verificação de uploads...")
    verificar_uploads()
