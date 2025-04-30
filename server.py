from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PROCESSADOS_FOLDER = "processados"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSADOS_FOLDER, exist_ok=True)

@app.route("/")
def upload_form():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'arquivo' not in request.files:
        return "Nenhum arquivo enviado."
    arquivo = request.files['arquivo']
    if arquivo.filename == '':
        return "Nome de arquivo vazio."
    caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
    arquivo.save(caminho)

    # Processar arquivo (simulando resultado aqui)
    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    resultado = ""
    for linha in linhas:
        resultado += f"Cena encontrada: {linha.strip()} (duração: 5 segundos)\n"

    nome_resultado = f"resultado_{arquivo.filename}"
    caminho_resultado = os.path.join(PROCESSADOS_FOLDER, nome_resultado)
    with open(caminho_resultado, "w", encoding="utf-8") as f:
        f.write(resultado)

    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard():
    arquivos = os.listdir(PROCESSADOS_FOLDER)
    return render_template("dashboard.html", arquivos=arquivos)

@app.route("/visualizar/<nome_arquivo>")
def ver_arquivo(nome_arquivo):
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if not os.path.exists(caminho):
        return "Arquivo não encontrado."
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    return f"<h2>Conteúdo de {nome_arquivo}</h2><pre>{conteudo}</pre>"

@app.route("/baixar/<nome_arquivo>")
def baixar_arquivo(nome_arquivo):
    return send_from_directory(PROCESSADOS_FOLDER, nome_arquivo, as_attachment=True)

@app.route("/excluir/<nome_arquivo>")
def excluir_arquivo(nome_arquivo):
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    app.run(debug=False)
