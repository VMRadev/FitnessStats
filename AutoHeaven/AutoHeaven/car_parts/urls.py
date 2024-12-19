from django.urls import path, include

from AutoHeaven.car_parts.views import CarPartDeleteView, CarPartUpdateView, CarPartCreateView, CarPartListView, \
    CarPartDetailView, notify_car_part_owner
from AutoHeaven.cars.views import CarUpdateView

urlpatterns = [
    path('', CarPartListView.as_view(), name='car-parts-list'),
    path('create/', CarPartCreateView.as_view(), name='car-part-create'),
    path('<int:car_part_pk>/<int:user_pk>/', notify_car_part_owner, name='notify-car-part-owner'),
    path('<int:pk>/', include([
        path('detail/', CarPartDetailView.as_view(), name='car-part-detail'),
        path('update/', CarPartUpdateView.as_view(), name='car-part-update'),
        path('delete/', CarPartDeleteView.as_view(), name='car-part-delete'),
    ]))
]
