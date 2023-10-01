import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

smtp_server = 'smtp.gmail.com'
smtp_port = 587 
smtp_user = 'yaneth33612@gmail.com' 
smtp_password = 'vekx ajac iaoa gwtw' 

mensaje = MIMEMultipart()
mensaje['From'] = 'yaneth33612@gmail.com'
mensaje['To'] = 'lorenayaneth33612@gmail.com'
mensaje['Subject'] = 'Test'

cuerpo = 'Correo enviado.'
mensaje.attach(MIMEText(cuerpo, 'plain'))

# imagen = open('imagen.jpg', 'rb').read()  
# imagen_adjunta = MIMEImage(imagen, name='imagen.jpg')
# mensaje.attach(imagen_adjunta)

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() 
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, mensaje['To'], mensaje.as_string())
    server.quit()
    print('Correo enviado correctamente')
except Exception as e:
    print(f'Error al enviar el correo: {str(e)}')
