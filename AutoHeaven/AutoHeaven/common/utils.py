from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

UserModel = get_user_model()

async def get_users_sender_receiver(user_sender, user_receiver):
    receiver = await UserModel.objects.select_related('profile').aget(pk=user_sender)
    sender = await UserModel.objects.select_related('profile').aget(pk=user_receiver)

    return receiver, sender


async def email_owner(subject, message, origin, to):
    await sync_to_async(send_mail)(
        subject=subject,
        message=message,
        from_email=origin,
        recipient_list=[to],
    )