from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AutoHeaven.car_parts.forms import CarPartCreateForm, CarPartUpdateForm
from AutoHeaven.car_parts.models import CarPart
from AutoHeaven.cars.forms import CarModelCreateForm, CarBrandCreateForm


class CarPartListView(LoginRequiredMixin, ListView):
    model = CarPart
    context_object_name = 'car_parts'
    template_name = 'car-parts/dashboard-car-parts.html'


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
    success_url = reverse_lazy('car-parts-list')

    




