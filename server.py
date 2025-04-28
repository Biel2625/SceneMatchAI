from flask import Flask, request, render_template_string
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processados'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# HTML da página principal
UPLOAD_PAGE = '''
<!doctype html>
<title>Upload de Roteiro</title>
<h1>Enviar Roteiro</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=arquivo>
  <input type=submit value=Enviar>
</form>
'''

# Página de resultado
RESULT_PAGE = '''
<!doctype html>
<title>Resultado do Processamento</title>
<h1>Resultado do seu roteiro:</h1>
<pre>{{resultado}}</pre>
<a href="/">Enviar outro roteiro</a>
'''

def processar_roteiro(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    resultado = []
    for linha in linhas:
        linha = linha.strip()
        if linha:
            resultado.append(f"Cena encontrada: {linha} (duração: 5 segundos)")

    nome_arquivo = os.path.basename(caminho_arquivo)
    resultado_nome = f"resultado_{nome_arquivo}"

    resultado_caminho = os.path.join(PROCESSED_FOLDER, resultado_nome)
    with open(resultado_caminho, 'w', encoding='utf-8') as f:
        f.write('\n'.join(resultado))

    return '\n'.join(resultado)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        arquivo = request.files['arquivo']
        if arquivo:
            caminho_arquivo = os.path.join(UPLOAD_FOLDER, arquivo.filename)
            arquivo.save(caminho_arquivo)
            resultado = processar_roteiro(caminho_arquivo)
            return render_template_string(RESULT_PAGE, resultado=resultado)
    return UPLOAD_PAGE

if __name__ == '__main__':
    app.run(debug=False)
