from flask import Flask, render_template, request, redirect, session, url_for
import os

app = Flask(__name__)
app.secret_key = 'chave_super_secreta'
UPLOAD_FOLDER = 'uploads'
PROCESSADOS_FOLDER = 'processados'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSADOS_FOLDER, exist_ok=True)

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        usuario = request.form.get('usuario', '')
        senha = request.form.get('senha', '')
        if usuario == 'admin' and senha == '1234':
            session['logado'] = True
            return redirect('/dashboard')
        else:
            erro = 'Usuário ou senha inválidos.'
    return render_template('login.html', erro=erro)

# Logout
@app.route('/logout')
def logout():
    session.pop('logado', None)
    return redirect('/login')

# Página de upload
@app.route('/', methods=['GET', 'POST'])
def upload():
    if not session.get('logado'):
        return redirect('/login')
    if request.method == 'POST':
        arquivo = request.files['roteiro']
        caminho = os.path.join(UPLOAD_FOLDER, arquivo.filename)
        arquivo.save(caminho)
        processar_arquivo(caminho)
        return redirect('/dashboard')
    return render_template('upload.html')

# Processamento fictício
def processar_arquivo(caminho):
    nome = os.path.basename(caminho)
    with open(caminho, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    resultado = [f"Cena encontrada: {linha.strip()} (duração: 5 segundos)\n" for linha in linhas]
    with open(os.path.join(PROCESSADOS_FOLDER, f"resultado_{nome}"), 'w', encoding='utf-8') as f:
        f.writelines(resultado)

# Dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('logado'):
        return redirect('/login')
    arquivos = os.listdir(PROCESSADOS_FOLDER)
    return render_template('dashboard.html', arquivos=arquivos)

# Visualizar conteúdo
@app.route('/visualizar/<nome_arquivo>')
def visualizar(nome_arquivo):
    if not session.get('logado'):
        return redirect('/login')
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        return f"<h2>Conteúdo de {nome_arquivo}</h2><pre>{conteudo}</pre>"
    return "Arquivo não encontrado.", 404

# Baixar arquivo
@app.route('/download/<nome_arquivo>')
def download_arquivo(nome_arquivo):
    if not session.get('logado'):
        return redirect('/login')
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        return open(caminho, 'rb').read()
    return "Arquivo não encontrado.", 404

# Excluir arquivo
@app.route('/excluir/<nome_arquivo>')
def excluir_arquivo(nome_arquivo):
    if not session.get('logado'):
        return redirect('/login')
    caminho = os.path.join(PROCESSADOS_FOLDER, nome_arquivo)
    if os.path.exists(caminho):
        os.remove(caminho)
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
