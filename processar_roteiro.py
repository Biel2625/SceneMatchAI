import os
import time

def processar_roteiro(nome_arquivo):
    """
    Simula o processamento de um roteiro e salva o resultado.
    """
    resultado = []

    print(f"Processando o roteiro '{nome_arquivo}'...")
    time.sleep(1)  # Simula o tempo de processamento

    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    for linha in linhas:
        linha = linha.strip()
        if linha:
            resultado.append(f"Cena encontrada: {linha} (duração: 5 segundos)")

    # Salvar resultado em um arquivo
    salvar_resultado(nome_arquivo, resultado)

    print("Processamento do roteiro concluído com sucesso!")

def salvar_resultado(nome_arquivo, resultados):
    """
    Salva as cenas encontradas em um arquivo resultado.txt
    """
    base_nome = os.path.splitext(os.path.basename(nome_arquivo))[0]
    nome_saida = f"resultado_{base_nome}.txt"

    with open(nome_saida, 'w', encoding='utf-8') as f:
        for linha in resultados:
            f.write(linha + '\n')

    print(f"Resultado salvo em: {nome_saida}")

def verificar_uploads():
    """
    Verifica se há arquivos de roteiro enviados.
    """
    uploads_dir = "uploads"
    if not os.path.exists(uploads_dir):
        print("Pasta de uploads não encontrada.")
        return

    arquivos = os.listdir(uploads_dir)
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith(".txt")]

    if not arquivos_txt:
        print("Nenhum roteiro encontrado.")
        return

    for roteiro in arquivos_txt:
        caminho = os.path.join(uploads_dir, roteiro)
        processar_roteiro(caminho)

if __name__ == "__main__":
    print("Iniciando verificação de uploads...")
    verificar_uploads()
