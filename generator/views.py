from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    return HttpResponse("Welcome home")


def sending_email(request):
    send_mail(
    'Subject here',
    'Here is the message.',
    settings.EMAIL_HOST_USER,
    ['somtochukwuuchegbu@gmail.com'],
    fail_silently=False,
)

    return HttpResponse("Your mail has been sent")