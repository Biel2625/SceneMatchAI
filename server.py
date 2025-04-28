from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Página de upload
@app.route('/upload.html', methods=['GET'])
def upload_page():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Upload de Roteiro</title>
    </head>
    <body style="text-align: center; margin-top: 100px;">
        <h1>Upload de Roteiro</h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="roteiro">
            <br><br>
            <input type="submit" value="Enviar Roteiro">
        </form>
    </body>
    </html>
    '''

# Lógica de upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'roteiro' not in request.files:
        return 'Nenhum arquivo enviado', 400

    file = request.files['roteiro']
    if file.filename == '':
        return 'Nenhum arquivo selecionado', 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return 'Roteiro enviado com sucesso!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
