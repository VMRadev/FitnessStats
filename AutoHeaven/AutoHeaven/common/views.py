from django.contrib.auth import get_user_model
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





