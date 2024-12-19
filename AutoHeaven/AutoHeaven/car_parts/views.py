from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AutoHeaven.car_parts.forms import CarPartCreateForm, CarPartUpdateForm
from AutoHeaven.car_parts.models import CarPart
from AutoHeaven.common.utils import get_users_sender_receiver, email_owner

UserModel = get_user_model()



class CarPartListView(LoginRequiredMixin, ListView):
    model = CarPart
    context_object_name = 'car_parts'
    template_name = 'car-parts/dashboard-car-parts.html'
    paginate_by = 8


class CarPartDetailView(LoginRequiredMixin, DetailView):
    model = CarPart
    context_object_name = 'car_part'
    template_name = 'car-parts/car-part-detail.html'


class CarPartCreateView(LoginRequiredMixin, CreateView):
    model = CarPart
    template_name = 'car-parts/car-part-create.html'
    form_class = CarPartCreateForm
    success_url = reverse_lazy('car-parts-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarPartDeleteView(LoginRequiredMixin, DeleteView):
    model = CarPart
    template_name = 'car-parts/car-part-delete.html'
    success_url = reverse_lazy('car-parts-list')


class CarPartUpdateView(LoginRequiredMixin, UpdateView):
    model = CarPart
    template_name = 'car-parts/car-part-update.html'
    form_class = CarPartUpdateForm
    context_object_name = 'car_part'
    success_url = reverse_lazy('car-parts-list')

async def fetch_users_and_car_part(request, user_pk, car_part_pk):
    car_part = await CarPart.objects.select_related('owner').aget(pk=car_part_pk)
    receiver, sender = await get_users_sender_receiver(car_part.owner.pk, user_pk)
    return car_part, receiver, sender


async def notify_car_part_owner(request, user_pk, car_part_pk):
    car_part, user_receiver, user_sender = await fetch_users_and_car_part(request, user_pk, car_part_pk)

    subject = f'{user_sender} seems to want to talk to you about {car_part}.'
    message=f"Hey {user_receiver}, I'm interested in the car part you are offering.\nCan we meet sometime?\nSo we could arrange a price?"

    await email_owner(
        subject,
        message,
        user_sender.email,
        user_receiver.email,
    )

    return await sync_to_async(redirect)('car-parts-list')





