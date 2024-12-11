from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AutoHeaven.cars.forms import CarCreateForm, CarModelCreateForm, CarBrandCreateForm, CarUpdateForm, \
    CarBrandUpdateForm, CarModelUpdateForm, CarSpecsEditForm
from AutoHeaven.cars.models import CarSpecs
from AutoHeaven.cars.models.app_car import Car, CarBrand, CarModel
from AutoHeaven.cars.utils import validate_model_and_brand_forms


class CarsListView(LoginRequiredMixin, ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'cars/dashboard.html'


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = 'car'
    template_name = 'cars/car-detail.html'


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'cars/car-create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_form_model'] = CarModelCreateForm(self.request.POST or None)
        context['car_form_brand'] = CarBrandCreateForm(self.request.POST or None)

        return context

    def form_valid(self, form):
        form = CarCreateForm(self.request.POST, self.request.FILES, )

        validate_model_and_brand_forms(self, form)

        return super().form_valid(form)

    def form_invalid(self, form):
        form_brand = CarBrandCreateForm(self.request.POST)
        form_model = CarModelCreateForm(self.request.POST)

        form_brand.is_valid()
        form_model.is_valid()

        return self.render_to_response(
            self.get_context_data(form=form, car_form_model=form_model, car_form_brand=form_brand)
        )


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'cars/car-delete.html'
    success_url = reverse_lazy('cars')


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'cars/car-update.html'
    form_class = CarUpdateForm
    success_url = reverse_lazy('cars')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_brand = context['car'].brand
        car_model = context['car'].model

        context['car_form_model'] = CarModelUpdateForm(instance=car_model)
        context['car_form_brand'] = CarBrandUpdateForm(instance=car_brand)

        return context

    def form_valid(self, form):
        form_brand = CarBrandUpdateForm(self.request.POST)
        form_model = CarModelUpdateForm(self.request.POST)

        if form.is_valid() and form_brand.is_valid() and form_model.is_valid():
            # Handle CarBrand
            brand_name = form_brand.cleaned_data['name']
            brand_obj, created = CarBrand.objects.get_or_create(name=brand_name)

            # Handle CarModel
            model_name = form_model.cleaned_data['model']
            model_obj, created = CarModel.objects.get_or_create(model=model_name, brand=brand_obj)

            # Associate brand and model with the car
            form.instance.brand = brand_obj
            form.instance.model = model_obj
            form.instance.owner = self.request.user  # Ensure owner is updated

            # Save the car object
            return super().form_valid(form)

        return self.form_invalid(form)

class CarSpecsUpdateView(LoginRequiredMixin, UpdateView):
    model = CarSpecs
    form_class = CarSpecsEditForm
    template_name = 'cars/car-specs-update.html'

    def get_success_url(self):
        return reverse_lazy('car-detail', kwargs={'pk': self.object.car.pk})

