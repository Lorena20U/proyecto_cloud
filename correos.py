from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Nombre del proyecto
# Mensaje 
# Categoría 

# Contacto
# Nombre del Product Owner
# Correo del PO
# Carrera del PO
# Teléfono del PO

def sender(recipent, categoria, creador, proyecto_actual): # mensaje, categorias
        #crea las instacias de objeto del mensaje
        msg = MIMEMultipart()
        message = f"Te saludamos desde CO&CO, \n\nSe ha agregado un proyecto nuevo en las siguientes áreas de tu interés:  {categoria}. \n\nNombre: {proyecto_actual['name']}\nObjetivo: {proyecto_actual['objetivo']}\nFecha_cierre: {proyecto_actual['fecha_cierre']}\nDescripcion: \n{proyecto_actual['descripcion']}\n \nPara más información contacta a:\n{creador['name']} {creador['last_name']}\n{creador['e_mail']}\n{creador['carrera']}\n{creador['celphone']}\n\n\nIngresa a CO&CO para enterarte de las últimas funciones."
    
        #ajustes de los parametros decorrespondiente correos
        password = "vekx ajac iaoa gwtw"
        msg['From'] = "yaneth33612@gmail.com"
        msg['Subject'] = f"Se agregó un nuevo proyecto. - CO&CO"
        ## Aquí habrá un for que llenará el Subject
    
        #cuerpo del mensaje
        msg.attach(MIMEText(message, 'plain'))
    
        #creacion del servidor
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
    
        #ingreso de credenciales para el correo
        server.login(msg['From'], password)
    
        #enviando mensajes
        for correo in recipent: 
            server.sendmail(msg['From'], correo, msg.as_string())
            print(f"Sent! : {correo}")

        server.quit()

"""
cs = [
    "danielbehar@ufm.edu", 
    "cldelcid@ufm.edu", 
    "cmalvarado@ufm.edu", 
    "alejandroreyes@ufm.edu", 
    "estebansamayoa@ufm.edu",
    "javiermazariegos@ufm.edu", 
    "lorenaperez@ufm.edu",
    "danielbeharaldana@gmail.com"
    ]
"""

# sender(cs)