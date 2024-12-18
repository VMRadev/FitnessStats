from celery import shared_task
from django.core.mail import send_mail


@shared_task
def notify_user_email(car, user, user_email):
    send_mail(
        subject=f'AutoHeaven has a new addition {car}.',
        message=f'Hey {user}, we just expanded the collection with a new addition {car}.',
        from_email='no-reply@autoheaven.com',
        recipient_list=[user_email],
    )

@shared_task
def notify_user_deletion_car(car, user, user_email):
    send_mail(
        subject=f'AutoHeaven sadly has lost {car}.',
        message=f'Hey {user}, we just have received the sad news that we are parting with {car}.',
        from_email='no-reply@autoheaven.com',
        recipient_list=[user_email],
    )