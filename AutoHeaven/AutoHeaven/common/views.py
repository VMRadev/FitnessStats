import asyncio

from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import ListView
from AutoHeaven.car_parts.models import CarPart
from AutoHeaven.cars.models import Car

UserModel = get_user_model()

# Create your views here.
class IndexView(ListView):
    template_name = 'common/index.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = Car.objects.all()
        context['car_parts'] = CarPart.objects.all()

        return context


async def fetch_users_and_car(request, car_id):
    users = await sync_to_async(UserModel.objects.filter)(car__isnull=False, car__not_id=car_id).exclude(car_id=car_id)
    car = await sync_to_async(Car.objects.get)(pk=car_id)
    return car, users

async def email_car_owners(subject, message, origin, to):
    await asyncio.sleep(10)
    await sync_to_async(send_mail)(
        subject=subject,
        message=message,
        from_email=origin,
        recipient_list=[to],
    )


async def notify_all_car_users(request, car_id):
    car, users = await fetch_users_and_car(request, car_id)

    subject = f'AutoHeaven has a new addition {car}'

    email_task = [
        email_car_owners(
            subject,
            f'Hey {user}, we just expanded the collection with a new addition {car}',
            'no-reply@autoheaven.com',
            user.email,
        )
        for user in users
    ]

    await asyncio.gather(*email_task)

    return redirect('cars')


