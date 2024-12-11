from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from AutoHeaven.cars.models import Car


# Create your views here.
class IndexView(ListView):
    template_name = 'common/index.html'
    model = Car

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context