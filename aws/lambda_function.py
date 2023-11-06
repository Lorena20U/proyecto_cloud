import json
import boto3
import time
from botocore.exceptions import ClientError

def sender(recipent, categoria, creador, proyecto_actual):
    SENDER = "Co&Co <yaneth33612@gmail.com>"
    RECIPIENT = recipent
    AWS_REGION = "us-east-1"
    
    SUBJECT = "Se agregó una nueva conferencia. - CO&CO"
    
    # The email body for recipients with non-HTML email clients.
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
    
    
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    
    try:
        #Provide the contents of the email.
        for correo in recipent: 
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        correo,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
            time.sleep(2)
    # Display an error if something goes wrong.	
    except ClientError as e:
        data = {"statusCode": 500,
            'body': json.dumps(e.response['Error']['Message'])
        }
        return data
    else:
        resultado = f'Enviados: {recipent}'
        data = {"statusCode": 200,
            'body': json.dumps(resultado)
        }   
        return data
        
def lambda_handler(event, context):
    recipent = eval(event['queryStringParameters']['recipent'])
    categoria = event['queryStringParameters']['categoria']
    creador = eval(event['queryStringParameters']['creador'])
    proyecto_actual = eval(event['queryStringParameters']['proyecto_actual'])
    return sender(recipent, categoria, creador, proyecto_actual)
