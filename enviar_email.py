import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, conteudo):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha_de_aplicativo"

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Resultado do processamento do seu roteiro"
    mensagem.attach(MIMEText(conteudo, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
            servidor.login(remetente, senha)
            servidor.send_message(mensagem)
        print("Email enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar email:", str(e))
