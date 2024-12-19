from django.contrib.auth import get_user_model
from django.dispatch import receiver

from AutoHeaven.cars.forms import CarModelCreateForm, CarBrandCreateForm
from AutoHeaven.cars.models import CarModel, CarBrand, Car

UserModel = get_user_model()

def validate_model_and_brand_forms(self, form):
    form_brand =CarBrandCreateForm(self.request.POST, )
    form_model = CarModelCreateForm(self.request.POST, )

    if form.is_valid() and form_brand.is_valid() and form_model.is_valid():
        brand_obj = CarBrand.objects.filter(name=form_brand.cleaned_data['name']).first()

        if not brand_obj:
            brand_obj = CarBrand.objects.create(name=form_brand.cleaned_data['name'])

        form.instance.brand = brand_obj
        form_model.brand = brand_obj

        model_obj = CarModel.objects.filter(model=form_model.cleaned_data['model']).first()

        if not model_obj:
            model_obj = CarModel.objects.create(model=form_model.cleaned_data['model'], brand=brand_obj)

        form.instance.model = model_obj
        form.instance.owner = self.request.user

        form.save()

    else:
        return self.render_to_response(
            self.get_context_data(form=form, car_form_model=form_model, car_form_brand=form_brand))


def get_users_car_id(user):
    users =  UserModel.objects.exclude(pk=user.pk)
    return users


