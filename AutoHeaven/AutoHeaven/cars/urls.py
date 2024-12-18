from django.urls import path, include
from AutoHeaven.cars.views import CarsListView, CarDetailView, CarDeleteView, CarUpdateView, CarCreateView, \
    CarSpecsUpdateView

urlpatterns = [
    path('', CarsListView.as_view(), name='cars'),
    path('create/', CarCreateView.as_view(), name='car-create'),
    # path('<int:pk>/', .as_view(), name='notify-users'),
    path('<int:pk>/', include([
        path('detail/', CarDetailView.as_view(), name='car-detail'),
        path('update/', CarUpdateView.as_view(), name='car-update'),
        path('update-specs/', CarSpecsUpdateView.as_view(), name='car-specs-update'),
        path('delete/', CarDeleteView.as_view(), name='car-delete'),
    ]))
]
