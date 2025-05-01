from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'segredo123'

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'processados'
ALLOWED_EXTENSIONS = {'txt'}
USUARIO = 'admin'
SENHA = '1234'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    if 'logado' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == USUARIO and senha == SENHA:
            session['logado'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erro='Credenciais inválidas')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'logado' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'Nenhum arquivo enviado'
        file = request.files['file']
        if file.filename == '':
            return 'Nenhum arquivo selecionado'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['RESULT_FOLDER'], f'resultado_{filename}'), 'w') as f:
                f.write("Cena encontrada: Jogador faz gol de bicicleta aos 89 minutos.\n")
            return redirect(url_for('dashboard'))
    return render_template('upload.html')

@app.route('/dashboard')
def dashboard():
    if 'logado' not in session:
        return redirect(url_for('login'))

    busca = request.args.get('busca', '').lower()
    pagina = int(request.args.get('pagina', 1))
    por_pagina = 5

    arquivos = [f for f in os.listdir(RESULT_FOLDER) if f.startswith('resultado_') and f.endswith('.txt')]
    if busca:
        arquivos = [f for f in arquivos if busca in f.lower()]
    total = len(arquivos)
    arquivos = sorted(arquivos)[(pagina-1)*por_pagina:pagina*por_pagina]

    return render_template('dashboard.html', arquivos=arquivos, busca=busca, pagina=pagina, total=total, por_pagina=por_pagina)

@app.route('/visualizar/<nome_arquivo>')
def visualizar_arquivo(nome_arquivo):
    if 'logado' not in session:
        return redirect(url_for('login'))
    caminho = os.path.join(RESULT_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        return render_template('visualizar.html', nome=nome_arquivo, conteudo=conteudo)
    return 'Arquivo não encontrado'

@app.route('/download/<nome_arquivo>')
def download_arquivo(nome_arquivo):
    if 'logado' not in session:
        return redirect(url_for('login'))
    return send_from_directory(RESULT_FOLDER, nome_arquivo, as_attachment=True)

@app.route('/excluir/<nome_arquivo>', methods=['POST'])
def excluir_arquivo(nome_arquivo):
    if 'logado' not in session:
        return redirect(url_for('login'))
    caminho = os.path.join(RESULT_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
