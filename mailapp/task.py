from celery import shared_task
import random
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_otp_email(email):
    otp_code = ''.join(random.choices('0123456789', k=6))  # Generate OTP code
    message = f"Your OTP code is: {otp_code}"
    send_mail('OTP Verification', message, settings.EMAIL_HOST_USER, [email])