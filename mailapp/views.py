from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .task import send_otp_email
import random

# Create your views here.


def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST["email"]
            send_otp_email.delay(email)
            messages.success(request, "Your account has been created successfullly")
            return redirect("index")
    return render(request, "signin.html", {"form": form})



# def send_otp_email(email):
#     otp_code = ''.join(random.choices('0123456789', k=6))  # Generate OTP code
#     message = f"Your OTP code is: {otp_code}"
#     send_mail('OTP Verification', message, settings.EMAIL_HOST_USER, [email])
