import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuração do e-mail (use variáveis de ambiente no Render!)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files or request.files['file'].filename == '':
        return "Arquivo inválido", 400

    file = request.files['file']
    email = request.form['email']

    # Salvar o conteúdo do arquivo (exemplo)
    content = file.read().decode('utf-8')
    result = f"Análise automática do roteiro:\n\n{content}"

    # Enviar resultado por e-mail
    try:
        msg = Message("Resultado do seu roteiro - SceneMatchAI",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=[email])
        msg.body = result
        mail.send(msg)
        return "Roteiro enviado com sucesso para seu e-mail!"
    except Exception as e:
        return f"Erro ao enviar e-mail: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
