import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os
import requests

def sender_ses(recipent, categoria, creador, proyecto_actual):
    # The API endpoint
    # url = f"https://n0g86wyeq5.execute-api.us-east-1.amazonaws.com/app?recipent={recipent}&categoria={categoria}&creador={creador}&proyecto_actual={proyecto_actual}"
    url = f"{os.environ['API_URL']}?recipent={recipent}&categoria={categoria}&creador={creador}&proyecto_actual={proyecto_actual}"
    print(url)
    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()