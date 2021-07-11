from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home_view(request):
<<<<<<< HEAD
    email = send_mail("Account confirmation mail", f"Click on the link to activate your account",
                      settings.EMAIL_HOST_USER, ["somtochukwuuchegbu@gmail.com"])
    return render(request, "email.html", context={})


def send_student_email(request):
    pass
=======
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
>>>>>>> f762aa6bb518583a0b1ce0fa594f654d01ead543
