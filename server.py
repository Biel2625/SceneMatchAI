from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Página de upload com estilo
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title>Upload de Roteiro - SceneMatchAI</title>
            <style>
                body {
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    font-family: Arial, sans-serif;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }
                h1 {
                    color: white;
                    margin-bottom: 20px;
                    text-shadow: 1px 1px 4px black;
                }
                form {
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                }
                input[type="file"] {
                    margin-bottom: 20px;
                }
                button {
                    background-color: #4facfe;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    font-size: 16px;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s ease;
                }
                button:hover {
                    background-color: #00c6fb;
                }
            </style>
        </head>
        <body>
            <h1>Enviar Roteiro</h1>
            <form method="POST" action="/upload" enctype="multipart/form-data">
                <input type="file" name="arquivo" required>
                <button type="submit">Enviar</button>
            </form>
        </body>
        </html>
    ''')

# Rota para processar o upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'arquivo' not in request.files:
        return 'Nenhum arquivo enviado!', 400
    file = request.files['arquivo']
    if file.filename == '':
        return 'Nenhum arquivo selecionado!', 400
    file.save(os.path.join(UPLOAD_FOLDER, file.filename))
    return f'<h2>Arquivo <strong>{file.filename}</strong> enviado com sucesso!</h2><br><a href="/">Enviar outro arquivo</a>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
