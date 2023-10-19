import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def sender_ses(recipent, categoria, creador, proyecto_actual):
    SENDER = "yaneth33612@gmail.com"
    SENDERNAME = "Co&Co"
    RECIPIENT = recipent
    USERNAME_SMTP = "AKIAXPYR246ICNXEWY74"
    PASSWORD_SMTP = "BGoCiFckyqjiCm7g+e+Dw8jEfqi3nbL9KZi3uv6UHV1Z"
    HOST = "email-smtp.us-east-1.amazonaws.com"
    PORT = 587

    SUBJECT = "Se agregó una nueva conferencia. - CO&CO"
    BODY_TEXT = f"Te saludamos desde CO&CO, \n\nSe ha agregado un proyecto nuevo en las siguientes áreas de tu interés:  {categoria}. \n\nNombre: {proyecto_actual['name']}\nObjetivo: {proyecto_actual['objetivo']}\nFecha_cierre: {proyecto_actual['fecha_cierre']}\nDescripcion: \n{proyecto_actual['descripcion']}\n \nPara más información contacta a:\n{creador['name']} {creador['last_name']}\n{creador['e_mail']}\n{creador['celphone']}\n\n\nIngresa a CO&CO para enterarte de las últimas funciones."

    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                "This email was sent with Amazon SES using the "
                "AWS SDK for Python (Boto)."
                )
                
    BODY_HTML = f"""<html>
    <head></head>
    <body>
    <h1>Te saludamos desde CO&CO</h1>
    <p>Se ha agregado un proyecto nuevo en las siguientes áreas de tu interés:  {categoria}.
    <br> Nombre: {proyecto_actual['name']}
    <br> Objetivo: {proyecto_actual['objetivo']}
    <br> Fecha_cierre: {proyecto_actual['fecha_cierre']}
    <br> Descripcion: 
    <br> {proyecto_actual['descripcion']}
    <br> Para más información contacta a:
    <br> {creador['name']} {creador['last_name']}
    <br> {creador['e_mail']}
    <br> {creador['celphone']}
    <br> Ingresa a CO&CO para enterarte de las últimas funciones.
    </p>
    </body>
    </html>
                """            

    msg = MIMEMultipart('alternative')
    msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
    # msg['To'] = RECIPIENT
    msg['Subject'] = SUBJECT

    part1 = MIMEText(BODY_TEXT, 'plain')
    part2 = MIMEText(BODY_HTML, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        # server.sendmail(SENDER, RECIPIENT, msg.as_string())
        for correo in recipent: 
            server.sendmail(SENDER, correo, msg.as_string())
            print(f"Sent! : {correo}")

        server.close()
    except Exception as e:
        print("Error :( ... ", e)
    else:
        print("Email sent!")