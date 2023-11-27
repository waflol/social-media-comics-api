from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def send_email(mail_subject, messages, recipients):
    email = EmailMessage(mail_subject, messages, to=recipients)
    email.content_subtype = "html"
    email.send(fail_silently=True)
