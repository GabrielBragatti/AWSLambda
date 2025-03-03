import boto3
import os

def lambda_handler(event, context):
    ses_client = boto3.client('ses', region_name='us-east-1')

    sender_email = "your-verified-email@example.com"
    recipient_email = "gabrielstocch@gmail.com"
    subject = "E-mail de teste AWS Lambda"
    body_text = "E-mail enviado de uma função Lambda"
    body_html = """<html>
    <head></head>
    <body>
      <h1>E-mail de teste do AWS Lambda</h1>
      <p>E-mail enviado de uma função Lambda</p>
    </body>
    </html>"""

    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [recipient_email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': "UTF-8",
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': "UTF-8",
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': "UTF-8",
                    'Data': subject,
                },
            },
            Source=sender_email,
        )
        return {
            'statusCode': 200,
            'body': 'Email sent!'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
