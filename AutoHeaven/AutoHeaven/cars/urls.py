from django.urls import path, include
from AutoHeaven.cars.views import CarsListView, CarDetailView, CarDeleteView, CarUpdateView, CarCreateView, \
    CarSpecsUpdateView, notify_car_owner

urlpatterns = [
    path('', CarsListView.as_view(), name='cars'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    path('<int:car_pk>/<int:user_pk>/', notify_car_owner, name='notify-car-owner'),
    path('<int:pk>/', include([
        path('detail/', CarDetailView.as_view(), name='car-detail'),
        path('update/', CarUpdateView.as_view(), name='car-update'),
        path('update-specs/', CarSpecsUpdateView.as_view(), name='car-specs-update'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ]))
]
