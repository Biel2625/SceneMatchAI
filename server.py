from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import os
from enviar_email import enviar_email

app = Flask(__name__)
app.secret_key = "segredo123"

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processados'
EMAIL_DESTINATARIO = 'obitogamer1997@gmail.com'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            session['logado'] = True
            return redirect(url_for('dashboard'))
        else:
            erro = "Usuário ou senha inválidos"
    return render_template('login.html', erro=erro)

@app.route('/dashboard')
def dashboard():
    if not session.get('logado'):
        return redirect(url_for('login'))
    arquivos = os.listdir(PROCESSED_FOLDER)
    return render_template('dashboard.html', arquivos=arquivos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        arquivo = request.files['arquivo']
        if arquivo:
            caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
            arquivo.save(caminho)

            # Simula o processamento (copiando para pasta processados)
            destino = os.path.join(PROCESSED_FOLDER, arquivo.filename)
            with open(caminho, 'r', encoding='utf-8') as origem, open(destino, 'w', encoding='utf-8') as destino_arquivo:
                destino_arquivo.write(origem.read())

            # Envia e-mail automaticamente
            enviar_email(EMAIL_DESTINATARIO, arquivo.filename)

            return redirect(url_for('dashboard'))
    return render_template('upload.html')

@app.route('/visualizar/<nome_arquivo>')
def visualizar(nome_arquivo):
    caminho = os.path.join(PROCESSED_FOLDER, nome_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    return render_template('visualizar.html', conteudo=conteudo)

@app.route('/baixar/<nome_arquivo>')
def baixar(nome_arquivo):
    return send_from_directory(PROCESSED_FOLDER, nome_arquivo, as_attachment=True)

@app.route('/excluir/<nome_arquivo>')
def excluir(nome_arquivo):
    caminho = os.path.join(PROCESSED_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
