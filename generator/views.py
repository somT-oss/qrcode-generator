from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    email = send_mail("Account confirmation mail", f"Click on the link to activate your account",
                      settings.EMAIL_HOST_USER, ["somtochukwuuchegbu@gmail.com"])
    return render(request, "email.html", context={})


def send_student_email(request):
    pass
