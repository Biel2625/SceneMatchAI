import os
import time
import subprocess

def monitorar_uploads():
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    
    print("Monitorando uploads na pasta 'uploads'...")
    
    while True:
        arquivos = os.listdir(uploads_dir)
        arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith('.txt')]
        
        if arquivos_txt:
            for arquivo in arquivos_txt:
                caminho_completo = os.path.join(uploads_dir, arquivo)
                print(f"Novo roteiro detectado: {arquivo}")
                
                # Chama o script processar_roteiro.py
                subprocess.run(["python", "processar_roteiro.py"])
                
                # Após processar, move o arquivo para a pasta 'processados' (vamos criar essa pasta também)
                processados_dir = os.path.join(os.getcwd(), 'processados')
                os.makedirs(processados_dir, exist_ok=True)
                os.rename(caminho_completo, os.path.join(processados_dir, arquivo))
                
                print(f"Roteiro '{arquivo}' processado e movido para a pasta 'processados'.")
        
        time.sleep(5)  # Verifica a cada 5 segundos

if __name__ == "__main__":
    monitorar_uploads()
