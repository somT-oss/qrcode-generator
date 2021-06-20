from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
    return HttpResponse("Your email has been sent")
