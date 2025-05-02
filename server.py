from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from enviar_email import enviar_email

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSADOS_FOLDER = 'processados'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        if usuario == 'admin' and senha == '1234':
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos')
    return render_template('login.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        arquivo = request.files['roteiro']
        if arquivo:
            caminho = os.path.join(app.config['UPLOAD_FOLDER'], arquivo.filename)
            arquivo.save(caminho)
            nome_processado = f'resultado_{arquivo.filename}'
            with open(os.path.join(PROCESSADOS_FOLDER, nome_processado), 'w') as f:
                f.write(f"Processado: {arquivo.filename}")
            enviar_email('destinatario@email.com', nome_processado)
            return redirect(url_for('dashboard'))
    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
    arquivos = os.listdir(PROCESSADOS_FOLDER)
    return render_template('dashboard.html', arquivos=arquivos)

@app.route('/ver_arquivo/<nome_arquivo>')
def ver_arquivo(nome_arquivo):
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    with open(caminho, 'r') as f:
        conteudo = f.read()
    return render_template('visualizar.html', conteudo=conteudo, nome_arquivo=nome_arquivo)

@app.route('/download_arquivo/<nome_arquivo>')
def download_arquivo(nome_arquivo):
    return send_from_directory(PROCESSADOS_FOLDER, nome_arquivo, as_attachment=True)

@app.route('/excluir_arquivo/<nome_arquivo>')
def excluir_arquivo(nome_arquivo):
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
