from flask import Flask, render_template, request, redirect, url_for
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Diretório onde os arquivos serão armazenados
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configuração de e-mail
EMAIL_USER = "seuemail@gmail.com"
EMAIL_PASSWORD = "suasenha"

def send_email(receiver_email, file_path):
    try:
        # Configurar o servidor SMTP
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = receiver_email
        msg['Subject'] = 'Roteiro Processado'

        # Corpo do e-mail
        body = f'O seu roteiro foi processado com sucesso. Clique no link abaixo para acessar o arquivo:\n{file_path}'
        msg.attach(MIMEText(body, 'plain'))

        # Enviar o e-mail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_USER, receiver_email, text)
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    email = request.form['email']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Enviar e-mail com o link para o arquivo
        file_path = url_for('static', filename=file.filename)
        send_email(email, file_path)
        
        return redirect(url_for('uploaded_file', filename=file.filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('upload_success.html', filename=filename)

if __name__ == "__main__":
    app.run(debug=True)