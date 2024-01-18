from django.core.mail import EmailMessage
import os

class Utils:
    @staticmethod
    def send_email(data):
        print(os.environ.get('EMAIL_FROM'))
        print(os.environ.get('EMAIL_USER'))
        print(os.environ.get('EMAIL_PASS'))
        email = EmailMessage(
        subject=data['subject'],
        body=data['body'],
        from_email=os.environ.get('EMAIL_FROM'),
        to=[data['to_email']]
        )
        email.send()