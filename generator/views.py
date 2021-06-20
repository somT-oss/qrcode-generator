from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
	email = send_mail(
    'Subject here',
    'Here is the message.',
    settings.EMAIL_HOST_USER,
    ['somtochukwuuchegbu@gmail.com'],
)
    return HttpResponse("Your email has been sent")
