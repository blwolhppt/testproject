from background_task import background
from django.core.mail import send_mail


@background
def send_email_task():
    send_mail(
        "Тема письма",
        "Привет",
        "obelova2003@yandex.ru",
        ["obelova2003@yandex.ru"],
        fail_silently=False,
    )
