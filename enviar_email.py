import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, nome_arquivo):
    remetente = "obitogamer1997@gmail.com"
    senha = "abcd efgh ijkl mnop"

    msg = MIMEMultipart()
    msg["From"] = remetente
    msg["To"] = destinatario
    msg["Subject"] = "Novo roteiro processado"

    corpo = f"O arquivo <strong>{nome_arquivo}</strong> foi processado com sucesso!"
    msg.attach(MIMEText(corpo, 'html'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(remetente, senha)
            servidor.send_message(msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
