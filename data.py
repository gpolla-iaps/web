from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import threading


uri = "mongodb+srv://empresa:azs3478ik@iaps.n01y9.mongodb.net/?retryWrites=true&w=majority&appName=Iaps"

cliente = "MyEmpresa"

db_clientes = "Clientes"
db_despachantes = "Despachantes"
db_exportadores = "Exportadores"
db_operaciones = "Operaciones"
db_usuario = "Usuarios"


def def_enviar_correo_nuevo_usuario(mail_usuario, nombre_usuario, apellido_usuario, fecha, hora, dialog) -> None:
    dialog.close()
    
    def enviar_correo():
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "app.fce.2024@gmail.com"  # Reemplaza con tu correo electrónico
        sender_password = "pvuk ldaa fczy jfcc"  # Reemplaza con tu contraseña o contraseña de aplicación

        # Dirección del destinatario
        receiver_email = "gpolla.iaps@gmail.com"  # Reemplaza con la dirección de destino

        # Creación del mensaje
        message = MIMEMultipart()  # Creación del mensaje
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Registro nuevo usuario"

        body = f"""
Hola:

Te informamos que un nuevo usuario se ha registrado en tu sitio web. Aquí tienes los detalles:

Nombre del usuario: {apellido_usuario}, {nombre_usuario}
Email del usuario: {mail_usuario}
Fecha de registro: Fecha {fecha} y Hora {hora} del Registro

Este mensaje es solo para notificarte del nuevo registro. Puedes consultar más información directamente en el panel de administración.

Saludos,
"""
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Iniciar conexión TLS (segura)
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()


    hilo_correo = threading.Thread(target = enviar_correo)
    hilo_correo.start()  # Iniciar el hilo (se ejecuta en segundo plano)




def def_enviar_correo_codigo(mail_usuario, codigo_verificacion) -> None:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "app.fce.2024@gmail.com"  # Reemplaza con tu correo electrónico
    sender_password = "pvuk ldaa fczy jfcc"  # Reemplaza con tu contraseña o contraseña de aplicación

    # Dirección del destinatario
    receiver_email = mail_usuario
    #receiver_email = "gpolla.iaps@gmail.com"  # Reemplaza con la dirección de destino

    # Creación del mensaje
    message = MIMEMultipart()  # Creación del mensaje
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Código de Verificación para tu Cuenta"

    body = f"""
Estimado/a usuario

Gracias por tu reciente solicitud. A continuación, encontrarás tu código de verificación:

Código de Verificación: {codigo_verificacion}

Por favor, ingresa este código en el campo correspondiente de nuestra aplicación para completar el proceso de verificación.

Si no solicitaste este código, por favor ignora este mensaje. Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en ponerte en contacto con nuestro equipo de soporte.

Gracias por tu atención.

Atentamente,
"""
    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Iniciar conexión TLS (segura)
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()