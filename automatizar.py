import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Carregar os dados dos clientes
clientes = pd.read_excel('./clientes.xlsx')

# Credenciais do Gmail
username = 'email@dominio.com'
gmail_password = 'senha'

# Iterar sobre cada cliente
for index, cliente in clientes.iterrows():
    email = cliente['E-mail']
    subject = 'Assunto do e-mail'
    body = 'Corpo do e-mail'

    # Construindo o email
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Enviar o email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, gmail_password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()