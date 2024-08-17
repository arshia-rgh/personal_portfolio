from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_email(email, name, message):
    send_mail(
        subject="Thank you for contacting us",
        message=f"Hi {name},\n\nThank you for reaching out to me. I have received your message:\n\n{message}\n\nBest regards,\nArshia.rgh",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[
            email,
        ],
        fail_silently=False,
    )
