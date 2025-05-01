from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

# Usuário e senha para login
USUARIO = "admin"
SENHA = "1234"

# Caminhos das pastas
UPLOAD_FOLDER = "uploads"
PROCESSADOS_FOLDER = "processados"

# Garante que as pastas existem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSADOS_FOLDER, exist_ok=True)

# Página inicial
@app.route("/")
def index():
    return redirect(url_for('login'))

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario == USUARIO and senha == SENHA:
            return redirect(url_for("dashboard"))
        else:
            erro = "Usuário ou senha inválidos"
    return render_template("login.html", erro=erro)

# Dashboard
@app.route("/dashboard")
def dashboard():
    arquivos = os.listdir(PROCESSADOS_FOLDER)
    return render_template("dashboard.html", arquivos=arquivos)

# Upload
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        arquivo = request.files["arquivo"]
        if arquivo:
            caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
            arquivo.save(caminho)
            return redirect(url_for("dashboard"))
    return render_template("upload.html")

# Visualizar
@app.route("/visualizar/<nome_arquivo>")
def visualizar_arquivo(nome_arquivo):
    caminho_arquivo = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()
        return render_template("visualizar.html", nome_arquivo=nome_arquivo, conteudo=conteudo)
    return "Arquivo não encontrado", 404

# Rota intermediária "Ver"
@app.route('/ver/<nome_arquivo>')
def ver_arquivo(nome_arquivo):
    return redirect(url_for('visualizar_arquivo', nome_arquivo=nome_arquivo))

# Baixar arquivo
@app.route("/download/<nome_arquivo>")
def download_arquivo(nome_arquivo):
    return send_from_directory(PROCESSADOS_FOLDER, nome_arquivo, as_attachment=True)

# Excluir arquivo
@app.route("/excluir/<nome_arquivo>")
def excluir_arquivo(nome_arquivo):
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(debug=True)
 